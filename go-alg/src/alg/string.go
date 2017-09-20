package alg

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"utils"
)

func op(opA float64, opB float64, opC string) (result float64, err error) {
	err = nil
	switch opC {
	case "+":
		result = opA + opB
	case "-":
		result = opA - opB
	case "/":
		if opB == 0 {
			result = 0
			err = errors.New("被除数不能为0")
		}
		result = opA / opB
	case "*":
		result = opA * opB
	default:
		result = 0
		err = errors.New("操作符不被识别")
	}
	return result, err
}

func EvaluateResversePolishNotation(ops []string) float64 {
	operations := "+-*/"

	stack := utils.NewStack()

	for _, s := range ops {
		if !strings.Contains(operations, s) {
			if f, err := strconv.ParseFloat(s, 64); err == nil {
				stack.Push(f)
			} else {
				fmt.Println("操作符不被识别")
				return 0
			}
		} else {
			f1, ok1 := stack.Pop().(float64)
			f2, ok2 := stack.Pop().(float64)
			if ok1 && ok2 {
				r, err := op(f1, f2, s)
				if err != nil {
					fmt.Println(err)
				}
				stack.Push(r)
			}
		}
	}

	result, ok := stack.Pop().(float64)

	if !ok {
		fmt.Println("Error")
		return 0
	}

	return result
}
