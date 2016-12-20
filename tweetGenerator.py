import random

def checkValidWord(word):
    return 'RT' not in word and '@' not in word and 'http' not in word and '\n' not in word and "#" not in word

def checkEndWord(word):
    return "." in word or "?" in word or "!" in word


def generateMessage():
    with open("twitterData.txt", "r", encoding='utf-8') as myfile:
        data = myfile.read()
    words= data.split(" ")
    startWords = [] #BOS
    endWords = [] #EOS
    ngrams = {} #Dictionary with words and followup words.

    for index in range(0, len(words)-1):
        if checkValidWord(words[index]) and checkValidWord(words[index+1]): #Check if it is a "real" word.
            if len(words[index]) > 0 and words[index][0].isupper(): #Words with uppercase letters
                startWords.append(words[index])
            if(checkEndWord(words[index])):
                endWords.append(words[index])
            if words[index] in ngrams and index != len(words):
                ngrams[words[index]].append(words[index + 1])
            elif index != len(words):
                ngrams[words[index]] = []
                ngrams[words[index]].append(words[index + 1])

    startWord = random.choice(startWords)
    output = startWord + " "
    for i in range(0,14):
        if(startWord in ngrams):
            newWord = random.choice(ngrams[startWord])
        else:
            newWord = random.choice(list(ngrams.keys()))
        output += newWord + " "
        startWord = newWord
    output += random.choice(endWords)
    return output


