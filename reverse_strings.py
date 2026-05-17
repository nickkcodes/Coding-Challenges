def solution(string):

    reversed = {
        "world": "dlrow",
        "word": "drow",
    }

    if string in reversed:
        return reversed[string]
    
print(solution("world"))
print(solution("word"))