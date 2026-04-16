package dev.revature.reportingservice.models;


import org.springframework.data.cassandra.core.cql.PrimaryKeyType;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyClass;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyColumn;

import java.io.Serializable;
import java.time.Instant;
import java.util.Objects;

@PrimaryKeyClass
public class CallsByAgentKey implements Serializable {

    @PrimaryKeyColumn(name="agent_id",ordinal = 0,type = PrimaryKeyType.PARTITIONED)
    private String agentId;

    @PrimaryKeyColumn(name="start_time",ordinal = 1, type = PrimaryKeyType.CLUSTERED)
    private Instant startTime;

    @PrimaryKeyColumn(name = "call_id", ordinal = 2, type = PrimaryKeyType.CLUSTERED)
    private String callId;

    public CallsByAgentKey() {
    }

    public CallsByAgentKey(String agentId, Instant startTime, String callId) {
        this.agentId = agentId;
        this.startTime = startTime;
        this.callId = callId;
    }

    @Override
    public String toString() {
        return "CallsByAgentKey{" +
                "agentId='" + agentId + '\'' +
                ", startTime=" + startTime +
                ", callId='" + callId + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CallsByAgentKey that = (CallsByAgentKey) o;
        return Objects.equals(agentId, that.agentId) && Objects.equals(startTime, that.startTime) && Objects.equals(callId, that.callId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(agentId, startTime, callId);
    }

    public String getAgentId() {
        return agentId;
    }

    public void setAgentId(String agentId) {
        this.agentId = agentId;
    }

    public Instant getStartTime() {
        return startTime;
    }

    public void setStartTime(Instant startTime) {
        this.startTime = startTime;
    }

    public String getCallId() {
        return callId;
    }

    public void setCallId(String callId) {
        this.callId = callId;
    }
}
