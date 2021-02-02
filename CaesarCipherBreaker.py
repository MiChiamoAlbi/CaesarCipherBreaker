import string
import math

probability = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def caesar(text, step, alphabets):

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

def entropy(text):
    tot = 0
    for i in range(len(string.ascii_lowercase)):
        h = (text.count(chr(97+i))+text.count(chr(65+i)))*math.log(probability[i])
        tot = h + tot

    return -tot
    

def main():
    text = str(input())
    h_min = 1000
    for i in range(len(string.ascii_lowercase)):
        phrase = caesar(text, i, (string.ascii_lowercase, string.ascii_uppercase))
        h = entropy(phrase)
        if h < h_min:
            h_min = h
            index = i

    print(caesar(text, index, (string.ascii_lowercase, string.ascii_uppercase)))

if __name__ == '__main__':
    main()

