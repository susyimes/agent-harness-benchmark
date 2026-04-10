import XCTest
@testable import LogInspector

final class ParserTests: XCTestCase {
    func testParseValidLine() throws {
        let parser = LogParser()
        let entry = try parser.parse("2026-03-01T10:24:01Z [ERROR] Payment failed orderId=O1009")
        XCTAssertEqual(entry.level, "ERROR")
    }

    func testMalformedLineShouldBeTolerated() throws {
        let parser = LogParser()
        XCTAssertNoThrow(try parser.parse("not-a-valid-log-line"))
    }
}
