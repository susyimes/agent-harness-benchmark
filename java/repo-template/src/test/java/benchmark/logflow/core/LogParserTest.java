package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class LogParserTest {
    @Test
    void parseBasicLine() {
        LogParser parser = new LogParser();
        LogEntry entry = parser.parse("2026-04-01T10:15:30Z INFO auth User login success", "app.log", 1);
        assertEquals("INFO", entry.level());
        assertEquals("auth", entry.service());
    }
}
