package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;

public class LogParser {
    public LogEntry parse(String line, String file, int lineNumber) {
        String[] parts = line.split(" ", 4);
        return new LogEntry(parts[0], parts[1], parts[2], parts[3], file, lineNumber);
    }
}
