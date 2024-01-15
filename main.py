from random import randint, choice


def get_randint():
    return [randint(1, 45) for _ in range(7)]


def get_choice():
    return [choice(range(1, 46)) for _ in range(7)]

if __name__ == '__main__':
    print(get_randint())
    print(get_choice())