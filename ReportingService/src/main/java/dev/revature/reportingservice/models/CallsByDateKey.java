package dev.revature.reportingservice.models;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.Instant;
import java.util.UUID;

import org.springframework.data.cassandra.core.cql.PrimaryKeyType;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyColumn;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyClass;

@PrimaryKeyClass
public class CallsByDateKey implements Serializable {

    @PrimaryKeyColumn(name = "call_date",ordinal = 0, type = PrimaryKeyType.PARTITIONED)
    private LocalDate callDate;

    @PrimaryKeyColumn(name = "start_time", ordinal = 1, type = PrimaryKeyType.CLUSTERED)
    private Instant startTime;

    @PrimaryKeyColumn(name = "call_id", ordinal = 2, type = PrimaryKeyType.PARTITIONED)
    private UUID callId;


    // Default constructor (required)
    public CallsByDateKey() {}

    public CallsByDateKey(LocalDate callDate, Instant startTime, UUID callId) {
        this.callDate = callDate;
        this.startTime = startTime;
        this.callId = callId;
    }

    // Getters and Setters

    public LocalDate getCallDate() {
        return callDate;
    }

    public void setCallDate(LocalDate callDate) {
        this.callDate = callDate;
    }

    public Instant getStartTime() {
        return startTime;
    }

    public void setStartTime(Instant startTime) {
        this.startTime = startTime;
    }

    public UUID getCallId() {
        return callId;
    }

    public void setCallId(UUID callId) {
        this.callId = callId;
    }

    // equals and hashCode (VERY IMPORTANT for Cassandra)

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof CallsByDateKey)) return false;

        CallsByDateKey that = (CallsByDateKey) o;

        if (!callDate.equals(that.callDate)) return false;
        if (!startTime.equals(that.startTime)) return false;
        return callId.equals(that.callId);
    }

    @Override
    public int hashCode() {
        int result = callDate.hashCode();
        result = 31 * result + startTime.hashCode();
        result = 31 * result + callId.hashCode();
        return result;
    }
}