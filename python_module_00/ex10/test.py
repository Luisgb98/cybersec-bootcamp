from loading import ft_progress
from time import sleep

X = range(3333)

if __name__ == "__main__":
    ret = 0
    for elem in ft_progress(X):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)