import json
import logging
from pathlib import Path
import jsonschema
from jsonschema import validate

# logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("etl_parser.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


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
            logger.error(f"Input directory does not exist: {self.input_dir}")
            return valid_transcripts
        for file_path in self.input_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    python_dict = json.load(f)

                validate(instance=python_dict, schema=self.schema)

                logger.info(f"{file_path.name}: JSON data is valid.")
                valid_transcripts.append(python_dict)

            except json.JSONDecodeError as e:
                logger.warning(f"{file_path.name}: invalid JSON - {e}")
            except jsonschema.exceptions.ValidationError as e:
                logger.warning(f"{file_path.name}: JSON data is invalid - {e.message}")
            except Exception as e:
                logger.error(f"{file_path.name}: unexpected error - {e}")
        return valid_transcripts
