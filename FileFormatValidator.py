import csv
import sys

def validate_file_format(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)

        # Validate header
        header = next(reader)
        expected_header = ["TB Id", "Medium", "Grade", "Subject", "Linked QR Count", "Resource Count"]
        if header != expected_header:
            print("Error: Invalid header row. Please ensure the file has the correct column names.")
            return

        # Define the master data for dimension values and metric value range
        master_dimensions = ["Accountancy", "Business Studies", "Civics","Creative Writing and Translation","Home Science","Health and Physical Education" ,"EVS","Urdu","Sanskrit","Sociology","Computer Science","SCIENCE","Sanskrit workbook","English", "Biology", "Chemistry", "Mathematics", "Physics", "Geography", "Urdu", "History", "Economics", "Computer Science", "Political Science", "Sociology", "Psychology", "Physical Education", "Fine Arts","HINDI","ENGLISH","Statistics","MATHS",""]

        metric_value_range = (0, 1000)

        # Validate each row
        row_number = 2  # Start from row 2 since we already read the header
        for row in reader:
            if len(row) != 6:
                print(f"Error: Invalid number of columns in row {row_number}.")
            else:
                # Validate specific columns
                tb_id = row[0]
                medium = row[1]
                grade = row[2]
                subject = row[3]
                linked_qr_count = row[4]
                resource_count = row[5]

                # Format check: Example format checks
                if not tb_id.startswith("do_"):
                    print(f"Error: Invalid TB Id format in row {row_number}.")
                if medium not in ["ENGLISH", "MATHS", "SCIENCE", "HINDI","URDU","SANSKRIT","Urdu","Sanskrit"]:
                    print(f"Error: Invalid Medium value in row {row_number}.")
                if not grade.startswith("Class"):
                    print(f"Error: Invalid Grade format in row {row_number}.")
                if not subject.lower() in [dimension.lower() for dimension in master_dimensions] and  not subject.upper() in [dimension.upper() for dimension in master_dimensions] and subject not in master_dimensions:
                    print(f"Error: Invalid Subject value in row {row_number}. Subject does not match the master data.")

                if not linked_qr_count.isdigit():
                    print(f"Error: Invalid Linked QR Count value in row {row_number}. Must be a non-negative integer.")
                if not resource_count.isdigit():
                    print(f"Error: Invalid Resource Count value in row {row_number}. Must be a non-negative integer.")

                # Completeness check: Ensure all required fields are filled
                if any(not field for field in row):
                    print(f"Error: Missing values in row {row_number}. All fields are required.")

                # Accuracy check: Add your accuracy checks here

                # Metric values check: Validate within range
                if not metric_value_range[0] <= int(linked_qr_count) <= metric_value_range[1]:
                    print(f"Error: Linked QR Count value out of range in row {row_number}.")
                if not metric_value_range[0] <= int(resource_count) <= metric_value_range[1]:
                    print(f"Error: Resource Count value out of range in row {row_number}.")

            row_number += 1

        # Display validation result
        print("File format validation completed.")

# Usage: python file_format_validator.py <file_path>
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_format_validator.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    validate_file_format(file_path)
