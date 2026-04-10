public struct RedactionService {
    public init() {}

    public func redact(_ text: String) -> String {
        return text.replacingOccurrences(of: #"\b\d{1,3}(?:\.\d{1,3}){3}\b"#, with: "[REDACTED_IP]", options: .regularExpression)
    }
}
