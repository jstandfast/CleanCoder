import os
import sys
from project_saver import ProjectSaver
from project_loader import PorjectLoader

def save_new_project():
    directory = input("Enter the directory path where the project is located: ")
    project_name = input("Enter the project name: ")

    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return None

    saver = ProjectSaver(directory, project_name)
    saver.save_project()

    print(f"Project '{project_name}' has been saved.")
    return project_name

def load_existing_project(project_name = None):

    if project_name == None:
        project_name = input("Enter the project name to load: ")

    loader = ProjectLoader(project_name)
    loader.load_project()

    print(f"Project '{project_name}' has been loaded.")
    return loaded_project

def exit_program():
    print("Exiting the program.")
    sys.exit()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Start new project")
        print("2. Open existing project")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            project = save_new_project()
            if project:
                load_existing_project(project)
                pass
        elif choice == '2':
            project = load_existing_project()
            if project:
                # Proceed with additional options for the opened project
                pass
        elif choice == '3':
            exit_program()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()