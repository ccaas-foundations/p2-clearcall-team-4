package dev.revature.reportingservice.repositories;

import dev.revature.reportingservice.models.CallsByAgents;
import dev.revature.reportingservice.models.CallsByCategory;
import dev.revature.reportingservice.models.CallsByCategoryKey;
import org.springframework.data.cassandra.repository.CassandraRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CallsByCategoryRepository extends CassandraRepository<CallsByCategory, CallsByCategoryKey> {
    List<CallsByCategory> findByKeyCallCategory(String callCategory);
}
