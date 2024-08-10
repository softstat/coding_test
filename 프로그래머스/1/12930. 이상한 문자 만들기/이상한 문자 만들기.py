def solution(s):
    answer = []
    words = s.split(" ")

    for word in words:
        converted_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                converted_word += char.upper()
            else:
                converted_word += char.lower()
        answer.append(converted_word)

    return " ".join(answer)
