from random import sample


def get_luckies():
    return sample(range(1, 46), k=6)

if __name__ == '__main__':
    print(get_luckies())