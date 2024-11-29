char=input("Enter a charecter")
def adding(char):
    if char.endswith("ing"):
        char=char.replace("ing","ly")
        return char
    else:
        char+="ing"
        return char
w=adding(char)
print(w)
