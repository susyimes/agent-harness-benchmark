package taskrunner

import "testing"

func TestRunUntilDoneBasic(t *testing.T) {
	cfg := Config{Tasks: []Task{{ID: "a", Action: "success"}, {ID: "b", Deps: []string{"a"}, Action: "success"}}}
	states := RunUntilDone(cfg, 10)
	if states["a"] != "success" || states["b"] != "success" {
		t.Fatalf("unexpected states: %+v", states)
	}
}

func TestTimeoutShouldFail(t *testing.T) {
	cfg := Config{Tasks: []Task{{ID: "slow", Action: "slow", Timeout: 10}}}
	states := RunUntilDone(cfg, 10)
	if states["slow"] != "failed" {
		t.Fatalf("expected failed, got %+v", states)
	}
}
