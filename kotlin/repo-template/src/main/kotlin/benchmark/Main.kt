package benchmark

fun main() {
    val config = RunnerConfig(
        tasks = listOf(
            TaskConfig(id = "a"),
            TaskConfig(id = "b", deps = listOf("a"))
        )
    )
    println(summarize(runUntilDone(config)))
}
