package benchmark

import kotlin.test.Test
import kotlin.test.assertEquals

class ReportFormatterTest {
    @Test
    fun summarizeCountsStates() {
        val summary = summarize(mapOf("a" to "success", "b" to "failed"))
        assertEquals(2, summary["total"])
        assertEquals(1, summary["success"])
        assertEquals(1, summary["failed"])
    }
}
