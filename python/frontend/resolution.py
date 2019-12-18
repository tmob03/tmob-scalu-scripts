
import copy

class resolution_block():
	variable_lookup = dict()
	constant_lookup = set()

def resolve(global_object):
	res = resolution_block()
	validate_block(global_object, res)
	resolve_block(global_object, res)
	return global_object


def resolution_error():
	raise Exception("Resolution error")


def validate_block(block, res):
	for ele in block.sequence:
		if ele.identity == "variable":
			validate_variable(res, ele)
		elif ele.identity == "assignment":
			validate_assignment(res, ele)
		else:
			resolution_error()


def resolve_block(block, res):
	for ele in block.sequence:
		if ele.identity == "assignment":
			resolve_assignment(res, ele)


def validate_variable(res, ele):
	if ele.name not in res.variable_lookup:
		res.variable_lookup[ele.name] = ele
	else:
		resolution_error()


def validate_assignment(res, ele):
	if ele.is_literal and (ele.destination in res.variable_lookup):
		res.constant_lookup.add((res.variable_lookup[ele.destination].type, ele.source))
	elif ele.source in res.variable_lookup and ele.destination in res.variable_lookup:
		pass
	else:
		resolution_error()


def resolve_assignment(res, ele):
	if ele.is_literal:
		ele.destination = res.variable_lookup[ele.destination]
		literal = copy.deepcopy(ele.destination)
		literal.name = ele.source
		literal.value = ele.source
		ele.source = literal
	else:
		ele.destination = res.variable_lookup[ele.destination]
		ele.source = res.variable_lookup[ele.source]