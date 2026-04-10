package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StatsService {
    public Map<String, Integer> countByLevel(List<LogEntry> entries) {
        Map<String, Integer> counts = new HashMap<>();
        for (LogEntry entry : entries) {
            counts.put(entry.level(), counts.getOrDefault(entry.level(), 0) + 1);
        }
        return counts;
    }
}
