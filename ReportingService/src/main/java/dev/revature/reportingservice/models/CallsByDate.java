package dev.revature.reportingservice.models;

import org.springframework.data.cassandra.core.mapping.Column;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

import java.util.Objects;

@Table("calls_by_date")
public class CallsByDate {

    @PrimaryKey
    private CallsByDateKey callsByDateKey;

    @Column("call_category")
    private String callCategory;

    @Column("ivr_contained")
    private boolean ivrContained;

    private boolean escalated;

    @Column("agent_id")
    private String agentId;

    @Column("duration_sec")
    private int durationSec;

    public CallsByDate() {
    }

    public CallsByDateKey getCallsByDateKey() {
        return callsByDateKey;
    }

    public void setCallsByDateKey(CallsByDateKey callsByDateKey) {
        this.callsByDateKey = callsByDateKey;
    }

    public String getCallCategory() {
        return callCategory;
    }

    public void setCallCategory(String callCategory) {
        this.callCategory = callCategory;
    }

    public boolean isIvrContained() {
        return ivrContained;
    }

    public void setIvrContained(boolean ivrContained) {
        this.ivrContained = ivrContained;
    }

    public boolean isEscalated() {
        return escalated;
    }

    public void setEscalated(boolean escalated) {
        this.escalated = escalated;
    }

    public String getAgentId() {
        return agentId;
    }

    public void setAgentId(String agentId) {
        this.agentId = agentId;
    }

    public int getDurationSec() {
        return durationSec;
    }

    public void setDurationSec(int durationSec) {
        this.durationSec = durationSec;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CallsByDate that = (CallsByDate) o;
        return ivrContained == that.ivrContained && escalated == that.escalated && durationSec == that.durationSec && Objects.equals(callsByDateKey, that.callsByDateKey) && Objects.equals(callCategory, that.callCategory) && Objects.equals(agentId, that.agentId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(callsByDateKey, callCategory, ivrContained, escalated, agentId, durationSec);
    }

    public CallsByDate(CallsByDateKey callsByDateKey, String callCategory, boolean ivrContained, boolean escalated, String agentId, int durationSec) {
        this.callsByDateKey = callsByDateKey;
        this.callCategory = callCategory;
        this.ivrContained = ivrContained;
        this.escalated = escalated;
        this.agentId = agentId;
        this.durationSec = durationSec;
    }

    @Override
    public String toString() {
        return "CallsByDate{" +
                "callsByDateKey=" + callsByDateKey +
                ", CallCategory='" + callCategory + '\'' +
                ", IvrContained=" + ivrContained +
                ", escalated=" + escalated +
                ", AgentId='" + agentId + '\'' +
                ", DurationSec=" + durationSec +
                '}';
    }
}
