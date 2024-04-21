import os
import shutil
folder_path = '/Your/Path/To/Downloads/Folder'
def organize_files_by_extension(folder_path):
    # Loop through each file in the directory
    for filename in os.listdir(folder_path):
        # Construct the absolute path of the file
        file_path = os.path.join(folder_path, filename)
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Extract file extension and define the destination subfolder
        file_extension = filename.split('.')[-1].lower()
        destination_folder = os.path.join(folder_path, file_extension)

        # Create the destination subfolder if it does not exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Relocate the file to its new subfolder
        shutil.move(file_path, destination_folder)

        print(f'Moved: {filename} to {destination_folder}/')
organize_files_by_extension(folder_path)
