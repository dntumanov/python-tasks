def count_letters(sentence: str, average: bool = False) -> int or float:
    """Возвращает количество букв в строке или в среднем на слово"""
    if average:
        words_list = sentence.split()
        count_average: float = count_character(sentence) / len(words_list)
        return round(count_average, 3)
    else:
        return count_character(sentence)


def count_character(sentence) -> int:
    """Возвращает количество букв в строке без учёта пробелов"""
    split_sentence = sentence.replace(" ", "")
    return len(split_sentence)


print(count_letters("I will build my own theme park"))
print(count_letters("I will build my own theme park", average=True))
