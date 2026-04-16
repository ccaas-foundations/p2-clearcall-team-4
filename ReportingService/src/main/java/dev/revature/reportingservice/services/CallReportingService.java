package dev.revature.reportingservice.services;

import dev.revature.reportingservice.models.CallsByAgents;
import dev.revature.reportingservice.models.CallsByDate;
import dev.revature.reportingservice.repositories.CallsByAgentsRepository;
import dev.revature.reportingservice.repositories.CallsByCategoryRepository;
import dev.revature.reportingservice.repositories.CallsByDateRepository;
import org.springframework.stereotype.Service;

import java.time.Instant;
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

    public List<CallsByDate> getCallsByDate(Instant date) {
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

//    public List<Double> getCallCountAndAverage(String agentId) {
//        List<CallsByAgents> calls = callsByAgentsRepository.findByKeyAgentId(agentId);
//
//        double callCount = calls.size();
//        double averageHandleTime = calls.stream()
//                .mapToDouble(CallsByAgents::getDurationSec)
//                .average()
//                .orElse(0.0);
//
//        return List.of(callCount, averageHandleTime);
//    }
}
