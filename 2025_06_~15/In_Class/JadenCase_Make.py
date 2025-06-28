def solution(s):
    words = s.split(" ")
    words = list(filter(lambda x: x != "", words))
    i = 0
    while i < len(words):
        words[i] = words[i].lower()
        words[i] = words[i].replace(words[i][0], words[i][0].upper(), 1)
        i += 1

    result = ""
    for n, i in enumerate(words):
        result += i
        if n != len(words) - 1:
            result += " "
    return result


print(solution("dd   ddd  fdgs    ds 3dg ddfssdf dfdsdfs  444 "))
