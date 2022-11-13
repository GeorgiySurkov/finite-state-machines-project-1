from typing import Iterator

Command = dict[str, int]
Program = list[Command]


def match(text: str) -> int:
    final_state = 6  # состояние, которое обозначает распознанный регулярный язык

    # program кодирует таблицу переходов конечного автомата.
    # Индекс в массиве обозначает состояние.
    # Словарь по индексу означает переход в следующее состояние
    # в зависимости от текущего символа.
    program: Program = [
        {"+": 1},
        {"+": 6, "a": 2, "b": 4},
        {"+": 6, "-": 3, "b": 4},
        {"a": 2},
        {"+": 6, "-": 5, "a": 2},
        {"b": 4},
    ]

    state = 0
    for i, ch in enumerate(text):
        possible_next_state = program[state].get(ch)
        if possible_next_state == final_state:
            return i + 1  # Конечный автомат распознал регулярный язык
        elif possible_next_state is None:
            return -1  # Конечный автомат не распознал регулярный язык
        else:
            state = possible_next_state
    return -1


def find_all_patterns(text: str) -> Iterator[tuple[int, int]]:
    for i in range(len(text)):
        end = match(text[i:])
        if end != -1:
            yield i, i + end


def main():
    text = input()
    no_patterns = True
    for begin, end in find_all_patterns(text):
        output = "{}: {}".format(begin + 1, text[begin:end])
        print(output)
        no_patterns = False
    if no_patterns:
        print("Цепочек не найдено")


if __name__ == '__main__':
    main()
