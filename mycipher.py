import sys

def shift_char(c, key):
    # shift A–Z by key with wraparound
    return chr((ord(c) - ord('A') + key) % 26 + ord('A'))

def main():
    # read key from command line
    key = int(sys.argv[1])

    # read all stdin into one string
    text = ""
    for line in sys.stdin:
        text += line

    # keep only A–Z, uppercase
    cleaned = ""
    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            cleaned += ch

    # apply Caesar shift
    encoded = "".join(shift_char(c, key) for c in cleaned)

    # print in blocks of 5 letters, 10 blocks per line
    count = 0
    for i in range(0, len(encoded), 5):
        block = encoded[i:i+5]
        print(block, end=" ")
        count += 1
        if count == 10:
            print()
            count = 0

    # final newline if needed
    if count != 0:
        print()

if __name__ == "__main__":
    main()
