import uuid

from cassandra.cluster import Cluster
from model import CallRecord

class CassandraLoader:
    def __init__(self, host: str, keyspace: str):
        self.host = host
        self.keyspace = keyspace
        self.cluster = None
        self.session = None

    def connect(self):
        self.cluster = Cluster(
            [self.host],
            port=9042
        )

        self.session = self.cluster.connect(self.keyspace)

        print("Connected!") 

    def load(self, record: CallRecord):
        self.session.execute("""
            INSERT INTO calls_by_date (
                call_date,
                start_time,
                call_id,
                call_category,
                ivr_contained,
                escalated,
                agent_id,
                duration_sec
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            record.call_date,
            record.start_time,
            uuid.UUID(record.call_id),
            record.call_category,
            record.ivr_contained,
            record.escalated_to_agent,
            record.agent_id,
            record.duration_seconds])
        
        self.session.execute("""
            INSERT INTO calls_by_agent(
                agent_id,
                start_time,
                call_id,
                call_category,
                duration_sec
                )
                VALUES (%s,%s,%s,%s,%s)
        """,[
            record.agent_id,
            record.start_time,
            uuid.UUID(record.call_id),
            record.call_category,
            record.duration_seconds])
        
        self.session.execute("""
            INSERT INTO calls_by_category(
                call_category,
                call_date,
                start_time,
                call_id,
                ivr_contained,
                duration_sec
                )
                VALUES (%s,%s,%s,%s,%s, %s)
        """,[
            record.call_category,
            record.call_date,
            record.start_time,
            uuid.UUID(record.call_id),
            record.ivr_contained,
            record.duration_seconds])


    def close(self):
        if self.cluster is not None:
            self.cluster.shutdown()
            print("Connection closed!")

        