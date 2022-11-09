def increment(x):
    return x + 1


def increment_v2(x): return x + 1


def higher_order_function(x, func):
    return x + func(x)


def higher_order_function_v2(x, func): return x + func(x)


result = higher_order_function(2, increment)
print(result)

result_v2 = higher_order_function_v2(2, increment_v2)
print(result_v2)

result_v3 = higher_order_function_v2(2, lambda x: x * 5)
print(result_v3)
