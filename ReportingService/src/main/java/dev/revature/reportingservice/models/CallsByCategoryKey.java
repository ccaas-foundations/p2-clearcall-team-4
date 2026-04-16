package dev.revature.reportingservice.models;


import org.springframework.data.cassandra.core.cql.PrimaryKeyType;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyClass;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyColumn;

import java.io.Serializable;
import java.time.Instant;
import java.util.Objects;
import java.util.UUID;

@PrimaryKeyClass
public class CallsByCategoryKey implements Serializable {

    @PrimaryKeyColumn(name="call_category",ordinal = 0,type = PrimaryKeyType.PARTITIONED)
    private String callCategory;

    @PrimaryKeyColumn(name="call_date",ordinal = 1, type = PrimaryKeyType.CLUSTERED)
    private Instant callDate;

    @PrimaryKeyColumn(name = "start_time", ordinal = 2, type = PrimaryKeyType.CLUSTERED)
    private Instant startTime;

    @PrimaryKeyColumn(name="call_id",ordinal = 3, type = PrimaryKeyType.CLUSTERED)
    private UUID callId;

    public CallsByCategoryKey() {
    }

    public CallsByCategoryKey(Instant callDate, String callCategory, Instant startTime, UUID callId) {
        this.callDate = callDate;
        this.callCategory = callCategory;
        this.startTime = startTime;
        this.callId = callId;
    }

    public String getCallCategory() {
        return callCategory;
    }

    public void setCallCategory(String callCategory) {
        this.callCategory = callCategory;
    }

    public Instant getCallDate() {
        return callDate;
    }

    public void setCallDate(Instant callDate) {
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

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CallsByCategoryKey that = (CallsByCategoryKey) o;
        return Objects.equals(callCategory, that.callCategory) && Objects.equals(callDate, that.callDate) && Objects.equals(startTime, that.startTime) && Objects.equals(callId, that.callId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(callCategory, callDate, startTime, callId);
    }

    @Override
    public String toString() {
        return "CallsByCategoryKey{" +
                "callCategory='" + callCategory + '\'' +
                ", callDate=" + callDate +
                ", startTime=" + startTime +
                ", callId=" + callId +
                '}';
    }


}
