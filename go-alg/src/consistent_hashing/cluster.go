package consistent_hashing


const AREA_SIZE_MAX uint32 = 1024

type Cluster struct {
	Areas []Area
	size uint32
}

func (cluster *Cluster) put(entry Entry) {
	index := entry.hashCode() % cluster.size
	cluster.Areas[index].put(entry)
}

func (cluster *Cluster) get(entry Entry) Entry {
	index := entry.hashCode() % cluster.size
	return cluster.Areas[index].get(entry)
}

func (cluster *Cluster) addArea(area Area) bool {
	if cluster.size > AREA_SIZE_MAX {
		return false
	}
	cluster.Areas = append(cluster.Areas, area)
	return true
}
