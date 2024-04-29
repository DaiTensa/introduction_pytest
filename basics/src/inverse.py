
def inverse(chaine):
    if isinstance(chaine, int):
        raise ValueError("Vous devez passer une chaine de caractère")
    
    for element in chaine:
        if not isinstance(element, str):
            raise ValueError("Vous devez passer une chaine de caractère")
    
    if len(chaine) == 4 and isinstance(chaine, list):
        chaine.pop()
    
    chaine = "".join(chaine)
    
    return chaine[::-1]


if __name__ == "__main__":
    print(inverse("hell"))
    # print(inverse(50))
    print(inverse(["a", "b"]))
    print(inverse(["a", "b", "c", "d"]))
    print(inverse(["a", 1]))
