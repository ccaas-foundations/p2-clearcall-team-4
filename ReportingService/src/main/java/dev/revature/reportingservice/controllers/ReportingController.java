package dev.revature.reportingservice.controllers;

import dev.revature.reportingservice.dtos.CategorySummary;
import dev.revature.reportingservice.models.CallsByAgents;
import dev.revature.reportingservice.models.CallsByCategory;
import dev.revature.reportingservice.models.CallsByDate;
import dev.revature.reportingservice.services.CallReportingService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
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
        return callReportingService.getCallsByAgent(agentId);
    }

    @GetMapping("/analytics/agents/{agentId}/handle-time")
    public double getAverageAgentHandleTime(@PathVariable String agentId){
        return callReportingService.getAverageHandleTime(agentId);
    }

    @GetMapping("/analytics/categories")
    public List<CategorySummary> getCallCountAndAverage(){
        return callReportingService.getCallCountAndAverage();
    }

    @GetMapping("/analytics/calls")
    public List<CallsByDate> getCallsByDate(@RequestParam(name = "date",required = true) Instant callDate){
        return callReportingService.getCallsByDate(callDate);
    }

}
