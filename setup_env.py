import subprocess
import sys
import os

def create_virtual_env(env_name):
    # Step 1: Create virtual environment
    subprocess.run([sys.executable, "-m", "venv", env_name])
    print(f"Virtual environment '{env_name}' created successfully.")

    # Activate the virtual environment
    if os.name == "nt":  # Windows
        activate_script = f"{env_name}\\Scripts\\activate"
    else:  # macOS and Linux
        activate_script = f"{env_name}/bin/activate"

    # Step 2: Install Django in the virtual environment
    subprocess.run([activate_script, "&&", "pip", "install", "django"], shell=True)
    print("Django installed successfully.")

# Run the function with your desired environment name
create_virtual_env("myenv")
