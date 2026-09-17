# The continue statement ends the current iteration and jumps to the
# top of the loop and starts the next iteration
while True:
    line = input('> ')

    if line[0] == '#':
        continue

    if line == 'done':
        break

    print(line)

print('Done!')
#Safer Version
#The above code will crash if the user simply presses Enter because line[0] does
#not exist for an empty string. A safer version is:
while True:
    line = input('> ')

    if len(line) > 0 and line[0] == '#':
        continue

    if line == 'done':
        break

    print(line)

print('Done!')