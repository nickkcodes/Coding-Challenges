def to_camel_case(text):
    words = text.replace("-", "_").split("_")

    return words[0] + "".join(word.capitalize() for word in words[1:])

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))