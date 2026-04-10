package taskrunner

import "testing"

func TestReadyTasksReturnsRoot(t *testing.T) {
	cfg := Config{Tasks: []Task{{ID: "a"}, {ID: "b", Deps: []string{"a"}}}}
	ready := ReadyTasks(cfg, map[string]string{})
	if len(ready) != 1 || ready[0].ID != "a" {
		t.Fatalf("unexpected ready tasks: %+v", ready)
	}
}

func TestReadyTasksShouldWaitAllDeps(t *testing.T) {
	cfg := Config{Tasks: []Task{{ID: "c", Deps: []string{"a", "b"}}}}
	ready := ReadyTasks(cfg, map[string]string{"a": "success", "b": "failed"})
	if len(ready) != 0 {
		t.Fatalf("expected no ready tasks, got %+v", ready)
	}
}
