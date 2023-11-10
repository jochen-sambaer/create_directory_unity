import os

def create_directory_structure(project_path):
    directories = [
        'Assets',
        'Assets/Scripts',
        'Assets/Scenes',
        'Assets/Models',
        'Assets/Textures',
        'Assets/Audio',
        'Assets/Animations',
        'Assets/Plugins',
        'Assets/Editor',
        'Assets/Resources',
        'Assets/Prefabs'
    ]

    for directory in directories:
        os.makedirs(os.path.join(project_path, directory), exist_ok=True)

    print('Directory structure created successfully.')

# Usage example
project_path = 'directory'
create_directory_structure(project_path)

import os
import shutil

def sort_files(project_path):
    for root, dirs, files in os.walk(project_path):
        files.sort()  # Sort files alphabetically

        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Sort files based on extension
            if file_name.endswith('.txt'):
                destination_dir = os.path.join(project_path, 'TextFiles')
            elif file_name.endswith('.png') or file_name.endswith('.jpg'):
                destination_dir = os.path.join(project_path, 'ImageFiles')
            elif file_name.endswith('.cs'):
                destination_dir = os.path.join(project_path, 'ScriptFiles')
            else:
                destination_dir = os.path.join(project_path, 'OtherFiles')

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)

            # Move the file to the destination directory
            shutil.move(file_path, destination_dir)

    print('Files sorted successfully.')



