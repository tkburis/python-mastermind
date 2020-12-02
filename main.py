from getpass import getpass
from random import randint


def gen_number():
    temp = list(map(int, str(randint(1, 9999))))
    if len(temp) == 4:
        return temp
    to_add = [0] * (4 - len(temp))
    to_add.extend(temp)
    return to_add


def get_input(a="guess"):  # so we don't need to repeat code to validate starting code and guesses
    while True:
        if a != "guess":
            input_code = getpass("Enter " + a + ": ")
        else:
            input_code = input("Enter " + a + ": ")

        if not input_code.isnumeric() or len(input_code) != 4:
            print("Make sure that this is entirely numeric and is 4 digits long")
            continue
        else:
            input_code = list(map(int, str(input_code)))
            break
    return input_code


t = int(input("Would you like to enter your own code (0) or have a random one generated (1)? "))
if t:
    target_code = gen_number()
    print("Generated code. Start guessing! \n")
else:
    target_code = get_input("starting code")

while True:
    current_guess = get_input()
    if current_guess != target_code:
        target_code_work = target_code[:]  # to avoid references
        b_to_print = 0
        w_to_print = 0

        for i in range(len(current_guess)):  # separating the for loops prioritises 'b', if a letter occurs multiple
                                             # times in the guess
            if current_guess[i] == target_code_work[i]:
                current_guess[i] = 'x'  # once a char has been worked on, replace with something else to avoid repeats
                target_code_work[i] = '*'  # I think this slightly bad algorithm is hard to avoid since we are operating
                b_to_print += 1            # 2 independent for loops, and keeping a list of worked on chars would be tedious

        for i in current_guess:
            if i in target_code_work:
                target_code_work[target_code_work.index(i)] = '*'
                w_to_print += 1

        print(('b' * b_to_print) + ('w' * w_to_print))
        continue
    else:
        print("Correct")
        break
