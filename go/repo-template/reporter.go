package taskrunner

import "sort"

func Summary(states map[string]string) map[string]int {
	result := map[string]int{"total": len(states), "success": 0, "failed": 0}
	for _, state := range states {
		if _, ok := result[state]; ok {
			result[state]++
		}
	}
	return result
}

func SortedIDs(states map[string]string) []string {
	ids := make([]string, 0, len(states))
	for id := range states {
		ids = append(ids, id)
	}
	sort.Strings(ids)
	return ids
}
