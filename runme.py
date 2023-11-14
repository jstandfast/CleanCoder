import os
import sys
from project_saver import ProjectSaver
#from source_file import *
#from file_partitioner import FilePartitioner
#import java_parser_listener

def load_new_project():
    directory = input("Enter the directory path where the project is located: ")
    project_name = input("Enter the project name: ")

    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return None

    scanner = ProjectSaver(directory, project_name)
    file_paths = scanner.scan_directory()

    for file in file_paths:
        print(str(file))

    # And then save them into a database
    # For example:
    # save_to_database(java_files, project_name)

    # The objects should also be kept in memory if the program will work with them
    # For now, let's assume the scanner returns a list of file paths for simplicity
    loaded_project = {'name': project_name, 'files': []}  # Replace with actual objects

    print(f"Project '{project_name}' has been loaded.")
    return loaded_project

def open_existing_project():
    project_name = input("Enter the project name to open: ")
    # Here you would retrieve the project's Java file objects from the database
    # For example:
    # project_data = load_from_database(project_name)

    # For now, let's assume we retrieve a list of file paths
    project_data = {'name': project_name, 'files': []}  # Replace with actual objects

    if project_data['files']:
        print(f"Project '{project_name}' is now open.")
    else:
        print(f"No project with the name '{project_name}' was found in the database.")
    return project_data

def exit_program():
    print("Exiting the program.")
    sys.exit()

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Load new project")
        print("2. Open existing project")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            project = load_new_project()
            if project:
                # Proceed with additional options for the loaded project
                pass
        elif choice == '2':
            project = open_existing_project()
            if project:
                # Proceed with additional options for the opened project
                pass
        elif choice == '3':
            exit_program()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()