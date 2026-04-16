package dev.revature.reportingservice.models;

import org.springframework.data.cassandra.core.mapping.Column;
import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

import java.util.Objects;

@Table("calls_by_category")
public class CallsByCategory {

    @PrimaryKey
    private CallsByCategoryKey key;

    @Column("ivr_contained")
    private boolean iveContained;

    @Column("duration_sec")
    private int durationSec;


    public CallsByCategory() {
    }

    public CallsByCategory(CallsByCategoryKey callsByCategoryKey, boolean iveContained, int durationSec) {
        this.key = callsByCategoryKey;
        this.iveContained = iveContained;
        this.durationSec = durationSec;
    }

    public CallsByCategoryKey getKey() {
        return key;
    }

    public void setKey(CallsByCategoryKey key) {
        this.key = key;
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
        return iveContained == that.iveContained && durationSec == that.durationSec && Objects.equals(key, that.key);
    }

    @Override
    public int hashCode() {
        return Objects.hash(key, iveContained, durationSec);
    }

    @Override
    public String toString() {
        return "CallsByCategory{" +
                "callsByCategoryKey=" + key +
                ", iveContained=" + iveContained +
                ", durationSec=" + durationSec +
                '}';
    }
}
