#!/usr/bin/env python3

# Jack Murphy
import operator
import readline
from termcolor import colored
import sys
import os

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)

		except RuntimeError:
			print("RuntimeError, restarting program")
			os.execv(sys.executable, ['python'] + sys.argv)

		except TypeError:
			print("TypeError, restarting program")
			os.execv(sys.executable, ['python'] + sys.argv)

		except NameError:
			print("NameError, restarting program")
			os.execv(sys.executable, ['python'] + sys.argv)

		except IndexError:
			print("IndexError, restarting program")
			os.execv(sys.executable, ['python'] + sys.argv)

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
