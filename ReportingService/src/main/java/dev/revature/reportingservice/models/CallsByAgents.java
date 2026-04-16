package dev.revature.reportingservice.models;

import org.springframework.data.cassandra.core.mapping.Column;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

import java.util.Objects;

@Table("calls_by_agent")
public class CallsByAgents {

    @PrimaryKey
    private CallsByAgentKey callsByAgentKey;

    @Column("call_category")
    private String callCategory;

    @Column("duration_sec")
    private int durationSec;


    @Override
    public String toString() {
        return "CallsByAgents{" +
                "callsByAgentKey=" + callsByAgentKey +
                ", callCategory='" + callCategory + '\'' +
                ", durationSec=" + durationSec +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CallsByAgents that = (CallsByAgents) o;
        return durationSec == that.durationSec && Objects.equals(callsByAgentKey, that.callsByAgentKey) && Objects.equals(callCategory, that.callCategory);
    }

    @Override
    public int hashCode() {
        return Objects.hash(callsByAgentKey, callCategory, durationSec);
    }

    public CallsByAgentKey getCallsByAgentKey() {
        return callsByAgentKey;
    }

    public void setCallsByAgentKey(CallsByAgentKey callsByAgentKey) {
        this.callsByAgentKey = callsByAgentKey;
    }

    public String getCallCategory() {
        return callCategory;
    }

    public void setCallCategory(String callCategory) {
        this.callCategory = callCategory;
    }

    public int getDurationSec() {
        return durationSec;
    }

    public void setDurationSec(int durationSec) {
        this.durationSec = durationSec;
    }

    public CallsByAgents() {
    }

    public CallsByAgents(CallsByAgentKey callsByAgentKey, String callCategory, int durationSec) {
        this.callsByAgentKey = callsByAgentKey;
        this.callCategory = callCategory;
        this.durationSec = durationSec;
    }
}
