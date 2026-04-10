function pickReadyTasks(tasks, states) {
  return tasks.filter((task) => {
    const deps = task.deps || [];
    if (deps.length === 0) return !states[task.id];
    return deps.some((dep) => states[dep] && states[dep].state === 'success') && !states[task.id];
  });
}

module.exports = { pickReadyTasks };
