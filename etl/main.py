from parser import TranscriptParser
from transformer import TranscriptTransformer

parser = TranscriptParser("../transcripts")
transformer = TranscriptTransformer()

transcripts = parser.validate_transcripts()

for transcript in transcripts:
    record = transformer.transform_transcript(transcript)
    print(record)