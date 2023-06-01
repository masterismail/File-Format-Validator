import csv
import os
def search_and_manipulate_text(search_text, replace_text, folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            # Create a temporary file to store the modified content
            temp_file = file_path + ".tmp"
            
            with open(file_path, 'r', newline='') as input_file, \
                    open(temp_file, 'w', newline='') as output_file:
                reader = csv.reader(input_file)
                writer = csv.writer(output_file)
                
                # Iterate over each row in the CSV file
                for row in reader:
                    modified_row = [cell.replace(search_text, replace_text) for cell in row]
                    writer.writerow(modified_row)
            
            # Replace the original file with the modified file
            os.replace(temp_file, file_path)
search_text = "Biology" # Enter the text to be searched
replace_text = "1" # Enter the text to be replaced
folder_path = r"C:\Users\moham\OneDrive\Desktop\File-Format-Validator\File-Format-Validator" # Enter the path of the folder containing CSV files

search_and_manipulate_text(search_text, replace_text,folder_path)
