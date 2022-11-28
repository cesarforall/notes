symbol = '#'
lines = range(1, 8)
symbolOutput = ''

print('#'*5)
print('')

for line in lines:
    print('#'*(4 - abs(4 - line)))