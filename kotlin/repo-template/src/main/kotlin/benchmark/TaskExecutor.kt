package benchmark

import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withTimeout

fun executeTask(task: TaskConfig) = runBlocking {
    when (task.action) {
        "fail" -> error("boom")
        "slow" -> {
            if (task.timeoutMs > 0) {
                withTimeout(task.timeoutMs) {
                    delay(150)
                }
            } else {
                delay(150)
            }
        }
        else -> Unit
    }
}

fun runOnce(config: RunnerConfig, states: MutableMap<String, String>): MutableMap<String, String> {
    val ready = readyTasks(config, states)
    if (ready.isEmpty()) return states
    val task = ready.first()
    try {
        executeTask(task)
        states[task.id] = "success"
    } catch (_: Exception) {
        states[task.id] = "failed"
    }
    return states
}

fun runUntilDone(config: RunnerConfig, maxSteps: Int = 100): Map<String, String> {
    val states = linkedMapOf<String, String>()
    repeat(maxSteps) {
        val before = states.size
        runOnce(config, states)
        if (states.size == before) return states
    }
    return states
}
