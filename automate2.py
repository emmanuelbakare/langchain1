import os
import shutil
import subprocess
import sys
import webbrowser
import time
import platform

def activate_virtual_environment():
    """Activate the virtual environment based on the operating system."""
    try:
        # Get the path to the virtual environment activation script
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
        
        if platform.system() == 'Windows':
            activate_script = os.path.join(base_path, 'activate.bat')
            activate_cmd = [activate_script]
        else:
            activate_script = os.path.join(base_path, 'activate')
            activate_cmd = ['source', activate_script]

        # Create a new shell with the virtual environment activated
        if platform.system() == 'Windows':
            subprocess.run(['cmd', '/c', activate_script], check=True)
        else:
            subprocess.run(['bash', '-c', f'source "{activate_script}"'], check=True)
        
        print("Virtual environment activated successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error activating virtual environment: {e}")
        return False
    except Exception as e:
        print(f"An error occurred while activating virtual environment: {e}")
        return False

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

def run_command(command, shell=False):
    """Run a command with the activated virtual environment."""
    try:
        # For Windows, we need to run commands through cmd.exe
        if platform.system() == 'Windows':
            if not shell:
                command = ['cmd', '/c'] + command
        
        result = subprocess.run(command, 
                              check=True, 
                              shell=shell,
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE,
                              text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def setup_django_project(app_name):
    """Set up a new Django project with the specified app name."""
    try:
        # First activate the virtual environment
        if not activate_virtual_environment():
            print("Failed to activate virtual environment. Exiting...")
            return

        # Step 1: Create and change to djangoapp directory
        project_dir = find_available_folder_name('djangoapp')
        os.makedirs(project_dir)
        os.chdir(project_dir)
        print(f"Created directory: {project_dir}")

        # Step 2: Create Django project
        if not run_command(['django-admin', 'startproject', 'core', '.']):
            return
        print("Created Django project: core")

        # Step 3: Create Django app
        if not run_command(['python', 'manage.py', 'startapp', app_name]):
            return
        print(f"Created Django app: {app_name}")

        # Step 4: Copy files from generated folder if it exists
        # script_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))
        source_dir = os.path.join(os.getcwd(), 'generated')  # 'generated' folder in the root directory
        destination_dir = os.path.join(os.getcwd(), project_dir, app_name)  # 'app_name' inside 'djangoapp'

        # Check if the source directory exists
        if not os.path.exists(source_dir):
            print(f"The source directory '{source_dir}' does not exist.")
        else:
            # Create the destination directory if it doesn't exist
            if not os.path.exists(destination_dir):
                print('cannot find destination directory - -creating it')
                os.makedirs(destination_dir)

            # Loop through all files in the source directory and copy them to the destination
            for filename in os.listdir(source_dir):
                source_file = os.path.join(source_dir, filename)
                destination_file = os.path.join(destination_dir, filename)
                
                if os.path.isfile(source_file):  # Ensure it's a file
                    shutil.copy(source_file, destination_file)
                    print(f"Copied: {filename}")
                else:
                    print(f"Skipping: {filename} (not a file)")
        # script_dir = os.path.abspath(os.getcwd())
        # generated_path = os.path.join(script_dir, 'generated')
        
        # if os.path.exists(generated_path):
        #     for item in os.listdir(generated_path):
        #         source = os.path.join(generated_path, item)
        #         destination = os.path.join(os.getcwd(), app_name, item)
                
        #         if os.path.isfile(source):
        #             shutil.copy2(source, destination)
        #         elif os.path.isdir(source):
        #             if os.path.exists(destination):
        #                 shutil.rmtree(destination)
        #             shutil.copytree(source, destination)
        #     print("Copied files from 'generated' folder")

        # Step 5: Update settings.py
        update_settings_file(os.getcwd(), app_name)
        print("Updated settings.py")

        # Step 6: Run migrations
        if not run_command(['python', 'manage.py', 'makemigrations']):
            return
        if not run_command(['python', 'manage.py', 'migrate']):
            return
        print("Applied database migrations")

        # Step 7 & 8: Start development server
        server_process = subprocess.Popen(['python', 'manage.py', 'runserver'],
                                        creationflags=subprocess.CREATE_NEW_CONSOLE if platform.system() == 'Windows' else 0)
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

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <app_name>")
        sys.exit(1)
    
    app_name = sys.argv[1]
    setup_django_project(app_name)