from random import randint, choice


def get_randint():
    return [randint(1, 50) for _ in range(7)]


def get_choice():
    return [choice(range(1, 51)) for _ in range(7)]


fruits = [
	'apple',
	'banana',
    'pineapple',
]

foods = [
	'pasta',
	'pizza',
    'stew',
]

if __name__ == '__main__':
    print(get_randint())
    print(get_choice())
