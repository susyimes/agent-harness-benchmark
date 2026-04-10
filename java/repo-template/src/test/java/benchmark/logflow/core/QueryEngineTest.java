package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class QueryEngineTest {
    @Test
    void searchShouldBeCaseInsensitiveByDefault() {
        QueryEngine engine = new QueryEngine();
        List<LogEntry> result = engine.search(List.of(
                new LogEntry("t", "ERROR", "billing", "Charge Failed", "app.log", 1)
        ), "failed", false);
        assertEquals(1, result.size());
    }

    @Test
    void searchShouldReturnNoResultForMissingKeyword() {
        QueryEngine engine = new QueryEngine();
        List<LogEntry> result = engine.search(List.of(
                new LogEntry("t", "INFO", "auth", "login ok", "app.log", 1)
        ), "error", false);
        assertEquals(0, result.size());
    }
}
