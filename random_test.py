def encode(strs) -> str:
    string = ""

    for word in strs:
        string += str(len(word)) + "#" + word
        
    return string 


print(encode(["Hello","World"]))