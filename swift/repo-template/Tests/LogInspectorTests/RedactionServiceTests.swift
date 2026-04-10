import XCTest
@testable import LogInspector

final class RedactionServiceTests: XCTestCase {
    func testRedactsIPv4() {
        let service = RedactionService()
        let output = service.redact("ip=192.168.1.10")
        XCTAssertEqual(output, "ip=[REDACTED_IP]")
    }

    func testRedactsCardToo() {
        let service = RedactionService()
        let output = service.redact("card=4111111111111111")
        XCTAssertNotEqual(output, "card=4111111111111111")
    }
}
