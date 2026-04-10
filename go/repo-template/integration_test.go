package taskrunner

import (
	"os"
	"testing"
)

func TestConfigFixturesBasic(t *testing.T) {
	data, err := os.ReadFile("testdata/configs/basic.json")
	if err != nil {
		t.Fatal(err)
	}
	cfg, err := ParseConfig(data)
	if err != nil {
		t.Fatal(err)
	}
	states := RunUntilDone(cfg, 10)
	if states["b"] != "success" {
		t.Fatalf("expected b success, got %+v", states)
	}
}
