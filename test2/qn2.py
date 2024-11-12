#multiplication table for agiven number
def print_multi_table(numb):
    for i in range(1, 13):
        print(f"{numb} x {i} = {numb * i}")
# we create an input for the number to use
numb = int(input("enter the number:"))

print_multi_table(numb)