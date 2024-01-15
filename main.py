from random import randint, choice


def get_randint():
    return [randint(1, 50) for _ in range(6)]


def get_choice():
    return [choice(range(1, 51)) for _ in range(6)]

if __name__ == '__main__':
    print(get_randint())
    print(get_choice())