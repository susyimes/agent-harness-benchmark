package benchmark

fun summarize(states: Map<String, String>): Map<String, Int> {
    val result = linkedMapOf("total" to states.size, "success" to 0, "failed" to 0)
    for (state in states.values) {
        if (result.containsKey(state)) {
            result[state] = result.getValue(state) + 1
        }
    }
    return result
}
