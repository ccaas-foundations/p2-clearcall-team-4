package dev.revature.reportingservice.models;

import org.springframework.data.cassandra.core.mapping.Column;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

import java.util.Objects;

@Table("calls_by_category")
public class CallsByCategory {

    @PrimaryKey
    private CallsByCategoryKey callsByCategoryKey;

    @Column("ivr_contained")
    private boolean iveContained;

    @Column("duration_sec")
    private int durationSec;


    public CallsByCategory() {
    }

    public CallsByCategory(CallsByCategoryKey callsByCategoryKey, boolean iveContained, int durationSec) {
        this.callsByCategoryKey = callsByCategoryKey;
        this.iveContained = iveContained;
        this.durationSec = durationSec;
    }

    public CallsByCategoryKey getCallsByCategoryKey() {
        return callsByCategoryKey;
    }

    public void setCallsByCategoryKey(CallsByCategoryKey callsByCategoryKey) {
        this.callsByCategoryKey = callsByCategoryKey;
    }

    public boolean isIveContained() {
        return iveContained;
    }

    public void setIveContained(boolean iveContained) {
        this.iveContained = iveContained;
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
        CallsByCategory that = (CallsByCategory) o;
        return iveContained == that.iveContained && durationSec == that.durationSec && Objects.equals(callsByCategoryKey, that.callsByCategoryKey);
    }

    @Override
    public int hashCode() {
        return Objects.hash(callsByCategoryKey, iveContained, durationSec);
    }

    @Override
    public String toString() {
        return "CallsByCategory{" +
                "callsByCategoryKey=" + callsByCategoryKey +
                ", iveContained=" + iveContained +
                ", durationSec=" + durationSec +
                '}';
    }
}
