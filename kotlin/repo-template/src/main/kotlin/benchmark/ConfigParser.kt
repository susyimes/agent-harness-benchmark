package benchmark

import kotlinx.serialization.Serializable

@Serializable
data class TaskConfig(
    val id: String,
    val deps: List<String> = emptyList(),
    val action: String = "success",
    val timeoutMs: Long = 0,
    val retry: Int = 0,
)

data class RunnerConfig(val tasks: List<TaskConfig>)
