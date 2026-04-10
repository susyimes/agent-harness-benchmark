package taskrunner

func ReadyTasks(cfg Config, states map[string]string) []Task {
	ready := []Task{}
	for _, task := range cfg.Tasks {
		if _, exists := states[task.ID]; exists {
			continue
		}
		if len(task.Deps) == 0 {
			ready = append(ready, task)
			continue
		}
		for _, dep := range task.Deps {
			if states[dep] == "success" {
				ready = append(ready, task)
				break
			}
		}
	}
	return ready
}
