package benchmark.logflow.io;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class FileScanner {
    public List<String> readLines(Path path) throws IOException {
        return Files.readAllLines(path);
    }
}
