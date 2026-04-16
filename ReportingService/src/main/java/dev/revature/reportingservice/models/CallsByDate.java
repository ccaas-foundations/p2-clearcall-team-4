package dev.revature.reportingservice.models;

import org.springframework.data.cassandra.core.mapping.PrimaryKey;
import org.springframework.data.cassandra.core.mapping.Table;

@Table("calls_by_date")
public class CallsByDate {

    @PrimaryKey
    private CallsByDateKey callsByDateKey;


}
