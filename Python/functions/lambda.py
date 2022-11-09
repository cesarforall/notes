# Lambda

def increment(x):
    return x + 1


def increment_v2(x): return x + 1


result = increment(10)
result_v2 = increment_v2(20)

print(result)
print(result_v2)


def full_name(
    name, last_name): return f'Full name is {name.title()} {last_name.title()}'


print(full_name('César', 'Almeida'))
