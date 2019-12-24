#!/usr/bin/env python3

import threading
import random
import os
import time

mutex = threading.Lock()

tree = list(open('tree2.txt').read().rstrip())


def colored_dot(color):
    if color == 'red':
        return f'\033[91m•\033[0m'
    if color == 'green':
        return f'\033[92m•\033[0m'
    if color == 'yellow':
        return f'\033[93m•\033[0m'
    if color == 'blue':
        return f'\033[94m•\033[0m'


def check_star(color):
    if color == 'yellow':
        return f'\033[93m•\033[0m'
    else:
        return '•'


def lights(color, indexes):
    off = True
    while True:
        for idx in indexes:
            tree[idx] = colored_dot(color) if off else '•'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()

        off = not off

        time.sleep(random.uniform(.5, 1.5))


yellow = []
red = []
green = []
blue = []

leaf = []
base = []



def main():
    for i, c in enumerate(tree):
        if c == 'Y':
            yellow.append(i)
            tree[i] = f'\033[93m•\033[0m'
        if c == 'R':
            red.append(i)
            tree[i] = '•'
        if c == 'G':
            green.append(i)
            tree[i] = '•'
        if c == 'B':
            blue.append(i)
            tree[i] = '•'
        if c == '\\':
            leaf.append(i)
            tree[i] = f'\033[32m\\\033[0m'
        if c == '/':
            leaf.append(i)
            tree[i] = f'\033[32m/\033[0m'
        if c == '_':
            leaf.append(i)
            tree[i] = f'\033[32m_\033[0m'
        if c == '[':
            base.append(i)
            tree[i] = f'\033[90m[\033[0m'
        if c == ']':
            base.append(i)
            tree[i] = f'\033[90m]\033[0m'
        if c == '=':
            leaf.append(i)
            tree[i] = f'\033[90m=\033[0m'


    ty = threading.Thread(target=lights, args=('yellow', yellow))
    tr = threading.Thread(target=lights, args=('red', red))
    tg = threading.Thread(target=lights, args=('green', green))
    tb = threading.Thread(target=lights, args=('blue', blue))

    # for t in [ty, tr, tg, tb]:
    for t in [tr, tg, tb]:
        t.start()
    # for t in [ty, tr, tg, tb]:
    for t in [tr, tg, tb]:
        t.join()


if __name__ == "__main__":
    main()
