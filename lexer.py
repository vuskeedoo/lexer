# CONSTANTS
LETTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT = "0123456789"
INPUTS = ["w", LETTER, DIGIT, "<", ">", "^",  "=", "!", "h", "i", "l", "e", "$"]

# DFSM function
def dfsm(input_string):
    table = {0: [1, 6, 7, 10, 13, 16, 18, 20, 6, 6, 6, 6, 6],
             1: [6, 6, 6, 22, 22, 22, 22, 22, 2, 6, 6, 6, 6],
             2: [6, 6, 6, 22, 22, 22, 22, 22, 6, 3, 6, 6, 6],
             3: [6, 6, 6, 22, 22, 22, 22, 22, 6, 6, 4, 6, 6],
             4: [6, 6, 6, 22, 22, 22, 22, 22, 6, 6, 6, 5, 6],
             5: [22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22],
             6: []}

    state = 0
    tokens = []
    print(state)
    for character in input_string:
        col = char_to_col(character)
        if state == 22:
            print("ERROR, invalid input")
            return False
        else:
            state = table[state][col]
            print("state = " + str(state) + "\tcharacter = " + character + "\tcol = " + str(col))

    if state == 5:
        tokens.append(("keyword", "while"))

    return tokens

# Gets column index from character
def char_to_col(character):
    return INPUTS.index(character)

# MAIN
if __name__ == "__main__":

    tokens = dfsm(input("Enter an input: "))
    if len(tokens) != 0:
        print("Terminated Successfully")
        print("Type\tToken")
        for token in tokens:
            print(token[0] + "\t" + token[1])
    else:
        print("Terminated in error: no tokens found")
