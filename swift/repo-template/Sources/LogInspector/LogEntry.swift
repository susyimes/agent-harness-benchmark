public struct LogEntry: Equatable {
    public let timestamp: String
    public let level: String
    public let message: String
    public let raw: String

    public init(timestamp: String, level: String, message: String, raw: String) {
        self.timestamp = timestamp
        self.level = level
        self.message = message
        self.raw = raw
    }
}
