import sys


def main():
    with open(sys.argv[1], 'rb') as op:
        decoded = op.read()
    res = ''.join(chr((ord(c) - i) % 256) for i, c in enumerate(decoded))
    print(res)


if __name__ == "__main__":
    main()
