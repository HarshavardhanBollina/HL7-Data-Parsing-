import hl7_parser
import json
import logging
import os

# Configure logging
logging.basicConfig(filename='logs/error.log', level=logging.INFO)

def parse_hl7_message(file_path):
    try:
        with open(file_path, 'r') as file:
            message = file.read()
        h = hl7_parser.parse(message)
        return h
    except hl7_parser.ParseException as e:
        logging.error(f"Parse error in HL7 message from {file_path}: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")
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
    data_folder = "/HL7-Data-Parsing-/sample_data"
    process_files(data_folder)
