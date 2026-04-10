public struct StatisticsService {
    public init() {}

    public func countByLevel(_ entries: [LogEntry]) -> [String: Int] {
        var result: [String: Int] = [:]
        for entry in entries {
            result[entry.level, default: 0] += 1
        }
        return result
    }
}
