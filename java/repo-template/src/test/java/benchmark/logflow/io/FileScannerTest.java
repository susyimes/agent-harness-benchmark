package benchmark.logflow.io;

import org.junit.jupiter.api.Test;

import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FileScannerTest {
    @Test
    void readsAppLog() throws Exception {
        FileScanner scanner = new FileScanner();
        assertEquals(3, scanner.readLines(Path.of("data/app.log")).size());
    }
}
