package dev.revature.reportingservice.controllers;

import dev.revature.reportingservice.models.CallsByAgents;
import dev.revature.reportingservice.models.CallsByDate;
import dev.revature.reportingservice.services.CallReportingService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.util.List;

@RestController
public class ReportingController {

    private final CallReportingService callReportingService;

    public ReportingController(CallReportingService callReportingService){
        this.callReportingService = callReportingService;
    }

    @GetMapping("/analytics/agents/{agentId}/calls")
    public List<CallsByAgents> getCallsByAgent(@PathVariable String agentId){
        return null;
    }

    @GetMapping("/analytics/agents/{agentId}/handle-time")
    public double getAverageAgentHandleTime(@PathVariable String agentId){
        return 0.0;
    }

    @GetMapping("/analytics/categories")
    public List<Double> getCallCountAndAverage(@PathVariable String agentId){
        return null;
    }

    @GetMapping("/analytics/calls?date={date}")
    public List<CallsByDate> getCallsByDate(@PathVariable Instant callDate){
        return null;
    }

}
