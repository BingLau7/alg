package utils

import (
	"strconv"
)

func Numberic(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}
