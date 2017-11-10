package normal


const AREA_SIZE_MAX uint32 = 1024

type Cluster struct {
	Areas []Area
	size uint32
}

func (cluster *Cluster) Put(entry Entry) {
	index := entry.hashCode() % cluster.size
	if cluster.Areas[index].entries == nil {
		cluster.Areas[index].entries = make(map[Entry]Entry)
	}
	cluster.Areas[index].put(entry)
}

func (cluster *Cluster) Get(entry Entry) Entry {
	index := entry.hashCode() % cluster.size
	return cluster.Areas[index].get(entry)
}

func (cluster *Cluster) AddArea(area Area) bool {
	if cluster.size > AREA_SIZE_MAX {
		return false
	}
	cluster.size++
	cluster.Areas[cluster.size] = area
	return true
}

func InitCluster() Cluster {
	return Cluster{Areas: make([]Area, AREA_SIZE_MAX), size:0}
}
