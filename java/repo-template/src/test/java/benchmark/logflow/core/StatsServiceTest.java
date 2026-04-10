package benchmark.logflow.core;

import benchmark.logflow.model.LogEntry;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

class StatsServiceTest {
    @Test
    void countLevels() {
        StatsService service = new StatsService();
        Map<String, Integer> counts = service.countByLevel(List.of(
                new LogEntry("t1", "INFO", "a", "m1", "app.log", 1),
                new LogEntry("t2", "ERROR", "a", "m2", "app.log", 2)
        ));
        assertEquals(1, counts.get("INFO"));
        assertEquals(1, counts.get("ERROR"));
    }
}
