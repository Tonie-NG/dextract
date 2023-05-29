import os
import zipfile

def extract_folder(zip_path, output_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    print("Extraction complete.")

# Specify the input compressed file and output directory
input_file = 'compressed_folder.zip'
output_directory = 'output_directory'

# Call the function to extract the folder
extract_folder(input_file, output_directory)
