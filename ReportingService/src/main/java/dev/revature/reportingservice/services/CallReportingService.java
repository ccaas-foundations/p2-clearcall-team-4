package dev.revature.reportingservice.services;

import dev.revature.reportingservice.dtos.CategorySummary;
import dev.revature.reportingservice.models.CallsByAgents;
import dev.revature.reportingservice.models.CallsByCategory;
import dev.revature.reportingservice.models.CallsByDate;
import dev.revature.reportingservice.repositories.CallsByAgentsRepository;
import dev.revature.reportingservice.repositories.CallsByCategoryRepository;
import dev.revature.reportingservice.repositories.CallsByDateRepository;
import org.springframework.stereotype.Service;

import java.time.Instant;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Service
public class CallReportingService {

    private final CallsByDateRepository callsByDateRepository;
    private final CallsByAgentsRepository callsByAgentsRepository;
    private final CallsByCategoryRepository callsByCategoryRepository;


    public CallReportingService(CallsByDateRepository callsByDateRepository, CallsByAgentsRepository callsByAgentsRepository, CallsByCategoryRepository callsByCategoryRepository) {
        this.callsByDateRepository = callsByDateRepository;
        this.callsByAgentsRepository = callsByAgentsRepository;
        this.callsByCategoryRepository = callsByCategoryRepository;
    }

    public List<CallsByDate> getCallsByDate(LocalDate date) {
        return callsByDateRepository.findByKeyCallDate(date);
    }

    public List<CallsByAgents> getCallsByAgent(String agentId) {
        return callsByAgentsRepository.findByKeyAgentId(agentId);
    }

    public double getAverageHandleTime(String agentId) {
        List<CallsByAgents> calls = callsByAgentsRepository.findByKeyAgentId(agentId);
        return calls.stream()
                .mapToInt(CallsByAgents::getDurationSec)
                .average()
                .orElse(0.0);
    }

    public List<CategorySummary> getCallCountAndAverage() {
        List<CategorySummary> summary = new ArrayList<>();
        String[] categories = {"GENERAL", "SALES", "TECHNICAL", "BILLING"};

        for(String category: categories){
            List<CallsByCategory> calls = callsByCategoryRepository.findByKeyCallCategory(category);
            long count = calls.size();
            int totalDuration = 0;
            for (CallsByCategory call : calls){
                totalDuration += call.getDurationSec();
            }
            double averageDuration = 0.0;
            if (count >0){
                averageDuration = (double) totalDuration /count;
            }
            CategorySummary result = new CategorySummary(category,count,averageDuration);
            summary.add(result);
        }

        return summary;
    }
}
