# Generators
# functions that can pause and resume their execution.
# Instead of using return, generators use the yield keyword.



def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

counter = count_up_to(5)
for number in counter:
    print(number) 


