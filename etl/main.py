from parser import TranscriptParser
from transformer import TranscriptTransformer
from loader import CassandraLoader
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Generate random call transcript JSON files.")
    parser.add_argument("-i",
                        "--input",
                        type=str,
                        default="./transcripts",
                        help="Input directory for transcript files (default: transcripts)"
                        )
    parser.add_argument("-H",
                        "--host",
                        type=str,
                        default="localhost",
                        help="Host for Cassandra Cluster (default: localhost)",
                        )
    parser.add_argument("-k",
                        "--keyspace",
                        type=str,
                        default="clearcall",
                        help="Keyspace in Cassandra Database (default: clearcall)",
                        )
    return parser.parse_args()

def main():
    args = parse_args()

    parser = TranscriptParser(args.input)
    transformer = TranscriptTransformer()
    loader = CassandraLoader(args.host,args.keyspace)

    transcripts = parser.validate_transcripts()
    loader.connect()

    for transcript in transcripts:
        record = transformer.transform_transcript(transcript)
        loader.load(record)

    loader.close()

if __name__ == "__main__":
    main()