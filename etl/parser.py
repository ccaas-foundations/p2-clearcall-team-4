import json
from pathlib import Path
import jsonschema
from jsonschema import validate

class TranscriptParser:
    def __init__(self, input_dir:str):
        self.input_dir = Path(input_dir)

        # Define a schema
        self.schema = {
            "type": "object",
            "properties": {
                "callId": {"type": "string"},
                "startTime": {"type": "string", "format": "date-time"},
                "endTime": {"type": "string", "format": "date-time"},
                "callCategory": {"type": "string"},
                "ivrContained": {"type": "boolean"},
                "escalatedToAgent": {"type": "boolean"},
                "agentId": {"type": ["string","null"]},
                "ivrPath": {
                    "type": "array",
                    "items": {"type":"string"}
                },

            },
            "required": ["callId", "startTime", "endTime", "callCategory", "ivrContained", "escalatedToAgent", "ivrPath"],
            "additionalProperties": False
        }
    def validate_transcripts(self):
        valid_transcripts = []
        if not self.input_dir.exists():
            print(f"Input directory does not exist: {self.input_dir}")
            return valid_transcripts
        for file_path in self.input_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    python_dict = json.load(f)

                validate(instance=python_dict, schema=self.schema)

                print(f"{file_path.name}: JSON data is valid.")
                valid_transcripts.append(python_dict)
            except jsonschema.exceptions.ValidationError as e:
                print(f"{file_path.name}: JSON data is invalid: {e.message}")




json_string = '{"callId": "4aa23055-9b14-4cf6-bc2d-11d979e67814","startTime": "2026-04-19T23:25:03Z","endTime": "2026-04-19T23:30:00Z","callCategory": "TECHNICAL","ivrContained": false,"escalatedToAgent": true,"agentId": "4","ivrPath": [    "WELCOME",    "BILLING",    "ACCOUNT_LOOKUP",    "RESOLVED"]}'
python_dict = json.loads(json_string)


try:
    validate(instance=python_dict, schema=schema)
    print("JSON data is valid.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON data is invalid: {e.message}")