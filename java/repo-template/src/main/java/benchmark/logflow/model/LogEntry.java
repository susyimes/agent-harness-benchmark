package benchmark.logflow.model;

public record LogEntry(String timestamp, String level, String service, String message, String file, int lineNumber) {}
