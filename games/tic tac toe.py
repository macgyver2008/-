import random
end = 0
count = 0
def simpan(tic_map) :
    if tic_map[0]== "o" and tic_map[1]== "o" and tic_map[3]== "o" :
        print("computer win")
    elif tic_map[3]== "o" and tic_map[4]== "o" and tic_map[5] == "o" :
        print("computer win")                                        # elif tic_map[4] == "o" and tic_map[5] == "o" and tic_map[6] == "o" :
    elif tic_map[6]== "o" and tic_map[7]== "o" and tic_map[8] == "o" :
        print("computer win")
    elif tic_map[0]== "o" and tic_map[3]== "o" and tic_map[6] == "o":
        print("computer win")
    elif tic_map[1]== "o" and tic_map[7]== "o" and tic_map[3] == "o":
        print("computer win")                                             # elif tic_map[4] == "o" and tic_map[5] == "o" and tic_map[6] == "o" :
    elif tic_map[2]== "o" and tic_map[5]== "o" and tic_map[8] == "o":
        print("computer win")
    elif tic_map[0]== "o" and tic_map[4]== "o" and tic_map[8] == "o":
        print("computer win")
    elif tic_map[2]== "o" and tic_map[4]== "o" and tic_map[6] == "o":
        print("computer win")

    if tic_map[0]== "x" and tic_map[1]== "x" and tic_map[3] == "x":
        print("You win")
    elif tic_map[3]== "x" and tic_map[4]== "x" and tic_map[5] == "x":
        print("You win")  # elif tic_map== "x"[4] == "o" and tic_map[5] == "o" and tic_map[6] == "o" :
    elif tic_map[6]== "x" and tic_map[7]== "x" and tic_map[8] == "x":
        print("You win")
    elif tic_map[0]== "x" and tic_map[3]== "x" and tic_map[6] == "x":
        print("You win")
    elif tic_map[1]== "x" and tic_map[7]== "x" and tic_map[3] == "x":
        print("You win")  # elif tic_map[4] == "o" and tic_map[5] == "o" and tic_map[6] == "o" :
    elif tic_map[2]== "x" and tic_map[5]== "x" and tic_map[8] == "x":
        print("You win")
    elif tic_map[0]== "x" and tic_map[4]== "x" and tic_map[8] == "x":
        print("You win")
    elif tic_map[2]== "x" and tic_map[4]== "x" and tic_map[6] == "x":
        print("You win")

def make_map() :
    tic_map = ["" for i in range(9)]            #tic_map = []
    return tic_map                              # for i in range(9):

def AI(tic_map) :
    while True:
        a = random.randrange(8)
        if tic_map[a] == "" :
            tic_map[a] = "o"
            return tic_map

def player(tic_map):
    while True:
         pos = int(input("1~9"))
         pos = pos - 1
         if tic_map[pos] == "" :
             tic_map[pos] = "x"
             return tic_map

def print_map(tic_map):
    print("-----------------")
    print(" | " + tic_map[0] + " | " + tic_map[1] + " | " + tic_map[2] + " | ")
    print(" | " + tic_map[3] + " | " + tic_map[4] + " | " + tic_map[5] + " | ")
    print(" | " + tic_map[6] + " | " + tic_map[7] + " | " + tic_map[8] + " | ")

tic_map = make_map()
print('player_x')
print("AI_o")
while True:
    tic_map = player(tic_map)

    print_map(tic_map)

    tic_map = AI(tic_map)

    print_map(tic_map)
    simpan(tic_map)
    for i in range(9):
        if not tic_map[i] == "":
            count += 1
    if count == 9:
        print('tie')
    else:
        count = 0
