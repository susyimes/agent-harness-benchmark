package main

import (
	"encoding/json"
	"fmt"
	"os"

	taskrunner "example.com/go-taskrunner-benchmark"
)

func main() {
	data, err := os.ReadFile("testdata/configs/basic.json")
	if err != nil {
		panic(err)
	}
	cfg, err := taskrunner.ParseConfig(data)
	if err != nil {
		panic(err)
	}
	states := taskrunner.RunUntilDone(cfg, 100)
	b, _ := json.Marshal(taskrunner.Summary(states))
	fmt.Println(string(b))
}
