package taskrunner

import "testing"

func TestParseConfig(t *testing.T) {
	cfg, err := ParseConfig([]byte(`{"tasks":[{"id":"a"}]}`))
	if err != nil {
		t.Fatal(err)
	}
	if len(cfg.Tasks) != 1 {
		t.Fatalf("expected 1 task, got %d", len(cfg.Tasks))
	}
}
