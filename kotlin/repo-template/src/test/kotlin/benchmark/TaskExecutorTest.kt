package benchmark

import kotlin.test.Test
import kotlin.test.assertEquals

class TaskExecutorTest {
    @Test
    fun runBasicChain() {
        val cfg = RunnerConfig(listOf(TaskConfig("a"), TaskConfig("b", deps = listOf("a"))))
        val states = runUntilDone(cfg)
        assertEquals("success", states["a"])
        assertEquals("success", states["b"])
    }

    @Test
    fun timeoutShouldFail() {
        val cfg = RunnerConfig(listOf(TaskConfig("slow", action = "slow", timeoutMs = 10)))
        val states = runUntilDone(cfg)
        assertEquals("failed", states["slow"])
    }
}
