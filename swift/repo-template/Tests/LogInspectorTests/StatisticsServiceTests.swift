import XCTest
@testable import LogInspector

final class StatisticsServiceTests: XCTestCase {
    func testCountLevels() {
        let service = StatisticsService()
        let counts = service.countByLevel([
            LogEntry(timestamp: "t1", level: "INFO", message: "m1", raw: ""),
            LogEntry(timestamp: "t2", level: "ERROR", message: "m2", raw: "")
        ])
        XCTAssertEqual(counts["INFO"], 1)
        XCTAssertEqual(counts["ERROR"], 1)
    }
}
