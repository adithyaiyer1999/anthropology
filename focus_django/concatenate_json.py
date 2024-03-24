import json


def concatenate_json_files(input_files, output_file):
    # Initialize an empty list to store combined data
    combined_data = []

    # Iterate over each input file
    for input_file in input_files:
        # Open the input file and load its contents
        with open(input_file, 'r') as file:
            data = json.load(file)

        # Append the loaded data to the combined list
        combined_data.extend(data)

    # Write the combined data to the output file
    with open(output_file, 'w') as file:
        json.dump(combined_data, file, indent=4)


# Example usage:
input_files = ['nomic_data.json', 'nomic_data_2.json', 'nomic_data_3.json', 'nomic_data_4.json']
output_file = 'combined_data.json'
concatenate_json_files(input_files, output_file)
