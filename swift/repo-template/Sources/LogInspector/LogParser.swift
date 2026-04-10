public enum LogParseError: Error {
    case invalidLine
}

public struct LogParser {
    public init() {}

    public func parse(_ line: String) throws -> LogEntry {
        let parts = line.split(separator: " ", maxSplits: 2).map(String.init)
        guard parts.count == 3 else { throw LogParseError.invalidLine }
        let timestamp = parts[0]
        let level = parts[1].replacingOccurrences(of: "[", with: "").replacingOccurrences(of: "]", with: "")
        let message = parts[2]
        return LogEntry(timestamp: timestamp, level: level, message: message, raw: line)
    }
}
