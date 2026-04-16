package dev.revature.reportingservice.dtos;

import java.util.Objects;

public class CategorySummary {
    private String callCategory;
    private long callCount;
    private double averageDuration;

    public CategorySummary() {
    }

    public CategorySummary(String callCategory, long callCount, double averageDuration) {
        this.callCategory = callCategory;
        this.callCount = callCount;
        this.averageDuration = averageDuration;
    }

    public String getCallCategory() {
        return callCategory;
    }

    public void setCallCategory(String callCategory) {
        this.callCategory = callCategory;
    }

    public long getCallCount() {
        return callCount;
    }

    public void setCallCount(long callCount) {
        this.callCount = callCount;
    }

    public double getAverageDuration() {
        return averageDuration;
    }

    public void setAverageDuration(double averageDuration) {
        this.averageDuration = averageDuration;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        CategorySummary that = (CategorySummary) o;
        return callCount == that.callCount && Double.compare(averageDuration, that.averageDuration) == 0 && Objects.equals(callCategory, that.callCategory);
    }

    @Override
    public int hashCode() {
        return Objects.hash(callCategory, callCount, averageDuration);
    }

    @Override
    public String toString() {
        return "CategorySummary{" +
                "callCategory='" + callCategory + '\'' +
                ", callCount=" + callCount +
                ", averageDuration=" + averageDuration +
                '}';
    }
}
