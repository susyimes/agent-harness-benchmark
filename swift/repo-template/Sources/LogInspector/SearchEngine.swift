public struct SearchEngine {
    public init() {}

    public func search(_ entries: [LogEntry], keyword: String, caseSensitive: Bool = true) -> [LogEntry] {
        let needle = caseSensitive ? keyword : keyword.lowercased()
        return entries.filter { entry in
            let hay = caseSensitive ? entry.message : entry.message.lowercased()
            return hay.contains(needle)
        }
    }
}
