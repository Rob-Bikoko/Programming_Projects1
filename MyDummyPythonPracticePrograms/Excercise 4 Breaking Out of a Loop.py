# The break statement ends the current loop and jumps to the statement
# immediately following the loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')