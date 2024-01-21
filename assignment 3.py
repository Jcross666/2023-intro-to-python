### Block comment goes here
#
#
#

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
guess_number = 1



def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

print(f"Possible colors are {' '.join(legal_colors)}\n")
print("please enter your guess with no spaces between colors. Colors cannot be repeated\n")

while True:
    guess =  input(f"guess {guess_number}: ")
    valid = True
    if len(guess) != 4:
        valid = False
        print("input needs to be four colors\n")
    elif len(set(guess)) != len(guess):
        valid = False
        print("you cant repeat colors, try again\n")
    else:
        for color in guess:
            if color not in legal_colors:
                valid = False
                print(f"{color} is not a valid color try again\n")
    if valid:
        if guess == ''.join(colors):
            print("\nyou win!")
            break
        elif guess_number == 5:
            print("\nyou lose!")
            break
        hint = ""
        for i in range(len(guess)):
            if guess[i] == colors[i]:
                hint += "R"
            elif guess[i] in colors:
                hint += "W"
            else:
                hint += "_"
        print(f"\n{hint}\n")
        guess_number += 1
    else:
        if guess_number == 5:
            print("you lose")
            break
    
    
        
        
    
