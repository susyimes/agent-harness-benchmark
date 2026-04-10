package benchmark.logflow.e2e;

import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertTrue;

class SearchApiE2ETest {
    @Test
    void applicationSearchPrintsErrorLine() throws Exception {
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream original = System.out;
        System.setOut(new PrintStream(out));
        try {
            benchmark.logflow.Application.main(new String[]{"search", "data/app.log", "failed"});
        } finally {
            System.setOut(original);
        }
        assertTrue(out.toString().contains("ERROR"));
    }
}
