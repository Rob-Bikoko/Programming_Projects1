#Question 1b Sum even numbers below a limit
#Develop sum_of_even_numbers(limit) to return the sum of all even numbers from 2 up to,
# but excluding, limit by using a for loop and range().
"""Step by step method
       Step 1. Create an accumulator named total and initialise it to 0.
       Step 2. Use range(2, limit, 2). The start value is 2, the stop value limit is excluded, and the step of 2 produces only even numbers.
       Step 3. Add each generated even number to total.
       Step 4. Return total after the loop finishes.

    """


def sum_of_even_numbers(limit):
    total = 0

    for number in range(2, limit, 2):
        total += number
        print( number )

    return total


print("Sum:", sum_of_even_numbers(10))

