import hl7  # Assuming you installed the 'hl7' library
import json
import logging
import os

# Ensure the logs directory exists
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(filename=os.path.join(log_directory, 'error.log'), level=logging.INFO)

def parse_hl7_message(file_path):
    try:
        with open(file_path, 'r') as file:
            message = file.read()
        h = hl7.parse(message)
        return h
    except Exception as e:  # Adjust this based on the library's documentation
        logging.error(f"Error in HL7 message from {file_path}: {e}")
    return None

def hl7_to_json(hl7_message):
    result = {}
    for segment in hl7_message:
        segment_name = str(segment[0])
        fields = []
        for field in segment[1:]:
            components = [str(component) for component in field]
            fields.append(components if len(components) > 1 else components[0])
        result[segment_name] = fields
    return json.dumps(result, indent=4)

def process_files(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith(".hl7"):
            file_path = os.path.join(data_folder, filename)
            parsed_message = parse_hl7_message(file_path)
            if parsed_message:
                json_output = hl7_to_json(parsed_message)
                print(f"JSON output for {filename}:\n{json_output}\n")

if __name__ == "__main__":
    data_folder = "sample_data"
    process_files(data_folder)
