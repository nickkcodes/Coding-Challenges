def boolean_to_string(b):

    words = {
        True: "Yes",
        False: "No",
    }

    if b in words:
        return words[b]
    
print(boolean_to_string(True))
print(boolean_to_string(False))