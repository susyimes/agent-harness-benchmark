package benchmark

import kotlin.test.Test
import kotlin.test.assertEquals

class DagSchedulerTest {
    @Test
    fun rootTaskIsReady() {
        val cfg = RunnerConfig(listOf(TaskConfig("a"), TaskConfig("b", deps = listOf("a"))))
        val ready = readyTasks(cfg, emptyMap())
        assertEquals(listOf("a"), ready.map { it.id })
    }

    @Test
    fun taskShouldWaitForAllDeps() {
        val cfg = RunnerConfig(listOf(TaskConfig("c", deps = listOf("a", "b"))))
        val ready = readyTasks(cfg, mapOf("a" to "success", "b" to "failed"))
        assertEquals(0, ready.size)
    }
}
