#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path

def check_and_manage_venv():
    # Default venv name and path
    venv_name = "venv"
    venv_path = Path(venv_name)
    
    # Check if venv exists
    if venv_path.exists() and (venv_path / "bin" / "python").exists():
        print(f"Virtual environment '{venv_name}' exists.")
        activate_choice = input("Do you want to activate it? (y/n): ").strip().lower()
        
        if activate_choice == 'y':
            # Print activation instructions since a script cannot modify parent shell environment
            shell_type = os.environ.get('SHELL', '').split('/')[-1]
            
            if shell_type == 'zsh':
                print(f"\nTo activate, run this command:\nsource {venv_name}/bin/activate\n")
            elif shell_type == 'bash':
                print(f"\nTo activate, run this command:\nsource {venv_name}/bin/activate\n")
            elif os.name == 'nt':  # Windows
                print(f"\nTo activate, run this command:\n{venv_name}\\Scripts\\activate\n")
            else:
                print(f"\nTo activate, run this command:\nsource {venv_name}/bin/activate\n")
        else:
            print("Not activating the virtual environment.")
    else:
        print(f"Virtual environment '{venv_name}' not found.")
        create_choice = input("Do you want to create a new one? (y/n): ").strip().lower()
        
        if create_choice == 'y':
            python_version = input("Enter Python version to use (e.g., 3.8, leave blank for default): ").strip()
            
            try:
                if python_version:
                    python_cmd = f"python{python_version}"
                    # Check if the specified Python version exists
                    try:
                        subprocess.run([python_cmd, "--version"], check=True, capture_output=True)
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        print(f"Python {python_version} not found. Using default Python.")
                        python_cmd = "python3"
                else:
                    python_cmd = "python3"
                
                # Create the virtual environment
                subprocess.run([python_cmd, "-m", "venv", venv_name], check=True)
                print(f"\nVirtual environment '{venv_name}' created successfully!")
                
                # Print activation instructions
                shell_type = os.environ.get('SHELL', '').split('/')[-1]
                
                if shell_type == 'zsh':
                    print(f"To activate, run this command:\nsource {venv_name}/bin/activate\n")
                elif shell_type == 'bash':
                    print(f"To activate, run this command:\nsource {venv_name}/bin/activate\n")
                elif os.name == 'nt':  # Windows
                    print(f"To activate, run this command:\n{venv_name}\\Scripts\\activate\n")
                else:
                    print(f"To activate, run this command:\nsource {venv_name}/bin/activate\n")
            
            except subprocess.CalledProcessError as e:
                print(f"Error creating virtual environment: {e}")
        else:
            print("Not creating a virtual environment.")

if __name__ == "__main__":
    check_and_manage_venv()