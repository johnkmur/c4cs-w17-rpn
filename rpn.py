#!/usr/bin/env python3

import operator
import readline
from colored import fg, bg, attr
from termcolor import colored

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

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
			#print('%s Result (is negative): %s' % (fg(1), attr(0)))
			print(colored("Result (is negative):", 'red'), colored(result, 'red'))
		elif (result == 0):
			print(colored("Result:", 'yellow'), colored(result, 'yellow'))
		else:
			print(colored("Result (is positive):", 'green'), colored(result, 'green'))
		# print ("Result: ", result)
		# print ('%s Hello World !!! %s' % (fg(1), attr(0)))
		#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

if __name__ == '__main__':
	main()
