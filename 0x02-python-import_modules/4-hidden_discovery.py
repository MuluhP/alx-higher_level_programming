#!/usr/bin/python3
import hidden_4


def main():
    a = dir(hidden_4)
    for index in range(len(a)):
        if(a[index][0] != '_'):
            print("{}".format(a[index]))


if __name__ == "__main__":
    main()
