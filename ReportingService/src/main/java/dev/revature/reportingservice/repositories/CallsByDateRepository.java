package dev.revature.reportingservice.repositories;

import dev.revature.reportingservice.models.CallsByCategory;
import dev.revature.reportingservice.models.CallsByDate;
import dev.revature.reportingservice.models.CallsByDateKey;
import org.springframework.data.cassandra.repository.CassandraRepository;
import org.springframework.stereotype.Repository;

import java.time.Instant;
import java.time.LocalDate;
import java.util.List;

@Repository
public interface CallsByDateRepository extends CassandraRepository<CallsByDate, CallsByDateKey> {
    List<CallsByDate> findByKeyCallDate(LocalDate callDate);
}
