import json
import jsonschema
from jsonschema import validate


# Define a schema
schema = {
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

json_string = '{"callId": "4aa23055-9b14-4cf6-bc2d-11d979e67814","startTime": "2026-04-19T23:25:03Z","endTime": "2026-04-19T23:30:00Z","callCategory": "TECHNICAL","ivrContained": false,"escalatedToAgent": true,"agentId": "4","ivrPath": [    "WELCOME",    "BILLING",    "ACCOUNT_LOOKUP",    "RESOLVED"]}'
python_dict = json.loads(json_string)

try:
    validate(instance=python_dict, schema=schema)
    print("JSON data is valid.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON data is invalid: {e.message}")