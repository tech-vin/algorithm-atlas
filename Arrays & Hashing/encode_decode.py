# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

def encode_string(obj):
    encode = ''
    for d in obj:
        word_len = len(d)
        encode += str(word_len) + '$#' + d 
    return encode

def decode_string(string):
    decode = []
    i = 0
    while i < len(string):
        j = i
        # find the length of the word
        while string[j] != '$':
            j += 1
        word_len = int(string[i:j])
        # move j to the start of the word
        j += 2 # skip '$#'
        # extract the word
        word = string[j:j+word_len] # 3 -> 7: neet
        decode.append(word)
        # move i to the next length position
        i = j + word_len # 3 + 4 = 7
    return decode

testcases = [
    ["neet","code","love","you"], #
    ["we","say",":","yes"],
]

print([encode_string(x) for x in testcases])
print(decode_string('4$#neet4$#code4$#love3$#you'))