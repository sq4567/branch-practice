from random import choice


def get_luckies():
    return [choice(range(1, 46)) for _ in range(6)]

if __name__ == '__main__':
    print(get_luckies())