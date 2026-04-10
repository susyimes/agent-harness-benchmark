package taskrunner

import "encoding/json"

type Task struct {
	ID      string   `json:"id"`
	Deps    []string `json:"deps,omitempty"`
	Action  string   `json:"action,omitempty"`
	Timeout int      `json:"timeout_ms,omitempty"`
	Retry   int      `json:"retry,omitempty"`
}

type Config struct {
	Tasks []Task `json:"tasks"`
}

func ParseConfig(data []byte) (Config, error) {
	var cfg Config
	err := json.Unmarshal(data, &cfg)
	return cfg, err
}
