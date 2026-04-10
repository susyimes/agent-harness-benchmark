import XCTest
@testable import LogInspector

final class SearchEngineTests: XCTestCase {
    func testSearchIsCaseInsensitiveByDefault() {
        let engine = SearchEngine()
        let entries = [LogEntry(timestamp: "t", level: "ERROR", message: "Payment Failed", raw: "")]
        let result = engine.search(entries, keyword: "failed", caseSensitive: false)
        XCTAssertEqual(result.count, 1)
    }

    func testSearchFindsNoMatch() {
        let engine = SearchEngine()
        let entries = [LogEntry(timestamp: "t", level: "INFO", message: "login ok", raw: "")]
        let result = engine.search(entries, keyword: "error", caseSensitive: false)
        XCTAssertEqual(result.count, 0)
    }
}
