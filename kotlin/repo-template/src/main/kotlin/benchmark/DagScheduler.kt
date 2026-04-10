package benchmark

fun readyTasks(config: RunnerConfig, states: Map<String, String>): List<TaskConfig> {
    return config.tasks.filter { task ->
        if (states.containsKey(task.id)) return@filter false
        if (task.deps.isEmpty()) return@filter true
        task.deps.any { dep -> states[dep] == "success" }
    }
}
