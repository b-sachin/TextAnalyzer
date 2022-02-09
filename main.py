# counting occurance of given character in given string
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def starting():
    # give your own file here'
    filename = "book.txt"
    text = ""
    l = []

    # Open file and read content for analysis
    with open(filename) as f:
        text = f.read()

    # counting percentage of each character in a given file
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text.lower(), char) / len(text)
        l.append("{0}|{1}={2}".format(char, char.upper(), round(perc, 2)))
    print(l)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    starting()

