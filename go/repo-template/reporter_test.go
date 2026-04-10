package taskrunner

import "testing"

func TestSummary(t *testing.T) {
	summary := Summary(map[string]string{"a": "success", "b": "failed"})
	if summary["total"] != 2 || summary["success"] != 1 || summary["failed"] != 1 {
		t.Fatalf("unexpected summary: %+v", summary)
	}
}
