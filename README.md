# File Format Validator

The File Format Validator is a command-line utility developed to validate CSV files based on a specified format. It ensures that the data in the files meets the required specifications, adheres to predefined rules, and provides clear error messages for any inconsistencies found.

## Features

- User-friendly interface: The utility provides a command-line interface (CLI) that allows users to easily validate CSV files.
- Format validation: It verifies that the file structure matches the specified format, including the column names and their order.
- Completeness check: The utility ensures that all the required fields in each row are filled, avoiding missing or incomplete data.
- Custom validation rules: Users can define their own custom validation rules specific to their data requirements.
- Error reporting: The utility provides clear and detailed error messages when a file fails validation, helping users identify and resolve issues effectively.

## Setup and Usage

1. Ensure you have Python installed (version 3.6 or higher).

2. Clone this repository:
`git clone https://github.com/yourusername/file-format-validator.git`

3. Install the required dependencies:
`pip install -r requirements.txt`


4. Prepare your input CSV file. The file should follow the specified format, with the column names in the correct order.

5. Run the File Format Validator:
`python file_format_validator.py <path_to_your_csv_file>`


6. The utility will validate the file and display the validation results, including any errors or inconsistencies found.

## Customization

You can customize the format specifications and add your own validation rules to meet your specific requirements. Modify the `file_format_validator.py` file to incorporate your custom checks or update the predefined rules.

## Limitations

- The utility currently supports CSV files as input. Support for other file formats may be added in the future.
- This utility focuses on format validation and basic checks. Additional functionalities like data cleaning, normalization, or integration with other systems are not included in this version.

## Contribution

Contributions to the File Format Validator project are welcome. If you encounter any issues or have suggestions for improvements, feel free to create a pull request or open an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
