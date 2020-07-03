import random

def print_dice(score):
    dice = ["[-----------]","[           ]","[           ]","[           ]","[-----------]"]
    if score == 1:
        dice[2] = "[     0     ]"
    elif score == 2:
        dice[1] = "[       0   ]"
        dice[3] = "[   0       ]"
    elif score == 3:
        dice[1] = "[       0   ]"
        dice[2] = "[     0     ]"
        dice[3] = "[   0       ]"
    elif score == 4:
        dice[1] = "[   0   0   ]"
        dice[3] = "[   0   0   ]"
    elif score == 5:
        dice[1] = "[   0   0   ]"
        dice[2] = "[     0     ]"
        dice[3] = "[   0   0   ]"
    elif score == 6:
        dice[1] = "[  0  0  0  ]"
        dice[3] = "[  0  0  0  ]"

    for i in dice:
        print(i)

ch = 'y'
while ch == 'y':
    score = random.randint(1,6)
    print_dice(score)
    ch = input("Want to roll again? y/n : ")