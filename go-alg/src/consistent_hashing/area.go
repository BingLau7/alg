package consistent_hashing

type Area struct {
	name string
	entries map[Entry]Entry
}

func (area *Area) put(e Entry) {
	area.entries[e] = e
}

func (area *Area) get(e Entry) Entry {
	return area.entries[e]
}
