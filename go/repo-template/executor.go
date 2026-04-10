package taskrunner

import (
	"context"
	"errors"
	"time"
)

func executeTask(ctx context.Context, task Task) error {
	switch task.Action {
	case "fail":
		return errors.New("boom")
	case "slow":
		select {
		case <-time.After(150 * time.Millisecond):
			return nil
		case <-ctx.Done():
			return nil
		}
	default:
		return nil
	}
}

func RunOnce(cfg Config, states map[string]string) map[string]string {
	ready := ReadyTasks(cfg, states)
	if len(ready) == 0 {
		return states
	}
	task := ready[0]
	ctx := context.Background()
	if task.Timeout > 0 {
		var cancel context.CancelFunc
		ctx, cancel = context.WithTimeout(ctx, time.Duration(task.Timeout)*time.Millisecond)
		defer cancel()
	}
	err := executeTask(ctx, task)
	if err != nil {
		states[task.ID] = "failed"
	} else {
		states[task.ID] = "success"
	}
	return states
}

func RunUntilDone(cfg Config, maxSteps int) map[string]string {
	states := map[string]string{}
	for i := 0; i < maxSteps; i++ {
		before := len(states)
		states = RunOnce(cfg, states)
		if len(states) == before {
			return states
		}
	}
	return states
}
