package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;

import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

public class QueryEngine {
    public List<LogEntry> search(List<LogEntry> entries, String keyword, boolean caseSensitive) {
        String expected = caseSensitive ? keyword : keyword.toLowerCase(Locale.ROOT);
        return entries.stream().filter(entry -> {
            String hay = caseSensitive ? entry.message() : entry.message().toLowerCase(Locale.ROOT);
            return hay.contains(expected);
        }).collect(Collectors.toList());
    }
}
