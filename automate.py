import os
import shutil
import subprocess
import sys
import webbrowser
import time

def find_available_folder_name(base_name):
    """Find an available folder name by appending numbers if necessary."""
    if not os.path.exists(base_name):
        return base_name
    
    counter = 1
    while True:
        new_name = f"{base_name}_{counter}"
        if not os.path.exists(new_name):
            return new_name
        counter += 1

def update_settings_file(project_path, app_name):
    """Update the INSTALLED_APPS in settings.py to include the new app."""
    settings_path = os.path.join(project_path, 'core', 'settings.py')
    
    with open(settings_path, 'r') as file:
        content = file.read()
    
    # Find the INSTALLED_APPS section and add the new app
    if 'INSTALLED_APPS = [' in content:
        apps_start = content.find('INSTALLED_APPS = [')
        apps_end = content.find(']', apps_start)
        
        # Insert the new app before the closing bracket
        new_content = (
            content[:apps_end].rstrip() +
            f"    '{app_name}',\n" +
            content[apps_end:]
        )
        
        with open(settings_path, 'w') as file:
            file.write(new_content)

def setup_django_project(app_name):
    """Set up a new Django project with the specified app name."""
    try:
        # Step 1: Create and change to djangoapp directory
        project_dir = find_available_folder_name('djangoapp')
        os.makedirs(project_dir)
        os.chdir(project_dir)
        print(f"Created directory: {project_dir}")
        print("current directory", os.getcwd())

        # Step 2: Create Django project
        subprocess.run(['django-admin', 'startproject', 'core', '.'], check=True)
        print("Created Django project: core")

        # Step 3: Create Django app
        print("Start creating app", app_name)
        subprocess.run(['python', 'manage.py', 'startapp', app_name], check=True)
        print(f"Created Django app: {app_name}")

        # Step 4: Copy files from generated folder if it exists
        script_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))
        generated_path = os.path.join(script_dir, 'generated')
        
        if os.path.exists(generated_path):
            for item in os.listdir(generated_path):
                source = os.path.join(generated_path, item)
                destination = os.path.join(os.getcwd(), app_name, item)
                
                if os.path.isfile(source):
                    shutil.copy2(source, destination)
                elif os.path.isdir(source):
                    if os.path.exists(destination):
                        shutil.rmtree(destination)
                    shutil.copytree(source, destination)
            print("Copied files from 'generated' folder")

        # Step 5: Update settings.py
        update_settings_file(os.getcwd(), app_name)
        print("Updated settings.py")

        # Step 6: Run migrations
        subprocess.run(['python', 'manage.py', 'makemigrations'], check=True)
        subprocess.run(['python', 'manage.py', 'migrate'], check=True)
        print("Applied database migrations")

        # Step 7 & 8: Start development server
        server_process = subprocess.Popen(['python', 'manage.py', 'runserver'])
        print("Started development server")

        # Step 9: Open web browser
        time.sleep(2)  # Wait for server to start
        webbrowser.open('http://127.0.0.1:8000/')
        print("Opened web browser")

        # Keep the script running until user interrupts
        print("\nPress Ctrl+C to stop the server and exit...")
        try:
            server_process.wait()
        except KeyboardInterrupt:
            server_process.terminate()
            print("\nServer stopped")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <app_name>")
        sys.exit(1)
    
    app_name = sys.argv[1]
    setup_django_project(app_name)