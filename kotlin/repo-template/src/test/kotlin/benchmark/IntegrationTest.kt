package benchmark

import kotlin.test.Test
import kotlin.test.assertEquals

class IntegrationTest {
    @Test
    fun runMixedChain() {
        val cfg = RunnerConfig(listOf(TaskConfig("a"), TaskConfig("b", deps = listOf("a"), action = "fail")))
        val states = runUntilDone(cfg)
        assertEquals("success", states["a"])
        assertEquals("failed", states["b"])
    }
}
