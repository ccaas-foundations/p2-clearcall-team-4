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
                end_time,
                call_category,
                ivr_contained,
                escalated_to_agent,
                agent_id,
                duration_seconds,
                ivr_path
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [
            record.call_date,
            record.start_time,
            record.call_id,
            record.end_time,
            record.call_category,
            record.ivr_contained,
            record.escalated_to_agent,
            record.agent_id,
            record.duration_seconds,
            record.ivr_path])

        self.session.execute("""
            INSERT INTO calls_by_agent(
                agent_id,
                start_time,
                call_id,
                call_category,
                duration_seconds
                )
                VALUES (%s,%s,%s,%s,%s)
        """,[
            record.agent_id,
            record.start_time,
            record.call_id,
            record.call_category,
            record.duration_seconds])
        
        self.session.execute("""
            INSERT INTO calls_by_category(
                call_cateogory,
                call_date,
                start_time,
                call_id,
                ivr_contained,
                duration_seconds
                )
                VALUES (%s,%s,%s,%s,%s, %s)
        """,[
            record.call_category,
            record.call_date,
            record.start_time,
            record.call_id,
            record.ivr_contained,
            record.duration_seconds])


    def close(self):
        if self.cluster is not None:
            self.cluster.shutdown()
            print("Connection closed!")

        