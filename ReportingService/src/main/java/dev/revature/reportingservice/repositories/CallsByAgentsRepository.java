package dev.revature.reportingservice.repositories;

import dev.revature.reportingservice.models.CallsByAgentKey;
import dev.revature.reportingservice.models.CallsByAgents;
import org.springframework.data.cassandra.repository.CassandraRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CallsByAgentsRepository extends CassandraRepository<CallsByAgents, CallsByAgentKey> {
    List<CallsByAgents> findByKeyAgentId(String agentId);
}
