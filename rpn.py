#!/usr/bin/env python3

import operator
import readline
from colored import fg, bg, attr
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		if (result < 0):
			print(colored("Result (is negative):", 'red'), colored(result, 'red'))
		elif (result == 0):
			print(colored("Result:", 'yellow'), colored(result, 'yellow'))
		else:
			print(colored("Result (is positive):", 'green'), colored(result, 'green'))

if __name__ == '__main__':
	main()
