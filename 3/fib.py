# -*- coding: utf-8 -*-

def main():
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a + b

if __name__ == '__main__': main()
