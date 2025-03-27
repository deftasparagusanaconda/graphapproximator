def console_clear():
        print("\033[2J\033[H", end='')

def console_clear_line():
        print("\033[1A\033[K\r", end='')

def get_input_graph_type(input_graph_type, InputGraphTypes):
	console_clear()

	while True:
		if input_graph_type is not None:
			print("input graph type =", InputGraphTypes(int(input_graph_type)).name.lower())
		else:
			print("input graph type =", input_graph_type)

		print()
		print("[0] - None")
		for inputgraphtype in InputGraphTypes:
			print(f"[{inputgraphtype.value}] - {inputgraphtype.name.lower()}")

		for i in range(10-len(InputGraphTypes)):
			print()
		
		print("[q] - back")
		print()
		output = input("choice: ")
		
		if '0' == output:
			return None
		
		if 'q' == output or 'back' == output:
			return input_graph_type
		
		if eval(output) not in InputGraphTypes:
			console_clear()
			continue
		else:
			break

	return output

def _get_input_graph_change(input_graph, input_graph_type, InputGraphTypes):
	output = input_graph

	if input_graph_type is None:
		print("set input graph type first")
		print()
		print("[Enter]")
		print()
		input("choice: ")
		return None

	elif int(input_graph_type) == InputGraphTypes.VALUES.value:
		console_clear_line()		
		output = input("input values: ")
		output = tuple(float(value) for value in output.split(','))	

	elif int(input_graph_type) == InputGraphTypes.POINTS.value:
		console_clear_line()		
		output = input("input points: ")
		output = output.replace(' ', '').split("),(")
		output = tuple(tuple(eval(thing.strip('()'))) for thing in output)

	elif int(input_graph_type) == InputGraphTypes.STRING.value:
		console_clear_line()		
		output = input("input string: ")

	else:
		input("error!")
	
	return output

def get_input_graph(input_graph, input_graph_type, InputGraphTypes):
	while True:
		console_clear()
		
#		print("input graph =", str(input_graph)[:66])
		print("input graph =", input_graph)
		print()
		print("[Enter] - change")
		print("[q]     - back")
		print()
		
		match input("choice: "):
			case '':	# same as just pressing [Enter]
				input_graph = _get_input_graph_change(input_graph, input_graph_type, InputGraphTypes)
			case 'q':
				return input_graph

	return input_graph

def get_func_interp(func_interp):
	return input("interpolation method: ")

def get_func_approx(func_approx):
	return input("approximation method: ")

def get_func_expr(func_expr):
	return input("expression function: ")

def get_func_iter_err_min_alg(func_iter_err_min_alg):
	return input("iterative error minimization algorithm: ")

def get_func_error(func_error):
	return input("error function: ")

def get_func_stepper(func_stepper):
	return input("stepper function: ")

def get_output_graph_type(output_graph_type, OutputGraphTypes):
	console_clear()

	while True:
		if output_graph_type is not None:
			print("output graph type =", OutputGraphTypes(int(output_graph_type)).name.lower())
		else:
			print("output graph type =", output_graph_type)

		print()
		print("[0] - None")
		for outputgraphtype in OutputGraphTypes:
			print(f"[{outputgraphtype.value}] - {outputgraphtype.name.lower()}")

		for i in range(10-len(OutputGraphTypes)):
			print()
		
		print("[q] - exit")
		print()
		output = input("choice: ")
		
		if '0' == output:
			return None
		
		if 'q' == output:
			return output_graph_type
		
		if eval(output) not in OutputGraphTypes:
			console_clear()
			continue
		else:
			break

	return output

"""
from enum import Enum
class InputGraphTypes(Enum):
        VALUES = 1
        POINTS = 2
        STRING = 3

var = get_input_graph(None, 3, InputGraphTypes)
print(var)
"""
