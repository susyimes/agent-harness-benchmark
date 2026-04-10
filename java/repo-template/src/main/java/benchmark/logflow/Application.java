package benchmark.logflow;

import benchmark.logflow.core.LogParser;
import benchmark.logflow.core.QueryEngine;
import benchmark.logflow.io.FileScanner;
import benchmark.logflow.model.LogEntry;

import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Application {
    public static void main(String[] args) throws Exception {
        if (args.length < 3 || !"search".equals(args[0])) {
            System.err.println("usage: search <file> <keyword>");
            System.exit(1);
        }
        Path file = Path.of(args[1]);
        String keyword = args[2];
        FileScanner scanner = new FileScanner();
        LogParser parser = new LogParser();
        List<LogEntry> entries = new ArrayList<>();
        int lineNumber = 1;
        for (String line : scanner.readLines(file)) {
            entries.add(parser.parse(line, file.toString(), lineNumber++));
        }
        QueryEngine engine = new QueryEngine();
        List<LogEntry> result = engine.search(entries, keyword, false);
        for (LogEntry entry : result) {
            System.out.println(entry.timestamp() + " " + entry.level() + " " + entry.message());
        }
    }
}
