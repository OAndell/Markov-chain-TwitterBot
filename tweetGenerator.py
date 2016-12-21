import random
import settings

def checkValidWord(word):
    return 'RT' not in word and '@' not in word and 'http' not in word and '\n' not in word and '#' not in word \
           and '&amp' not in word and '…' not in word

def checkEndWord(word):
    return "." in word or "?" in word or "!" in word


def generateMessage():
    with open(settings.getDataFileName(), "r", encoding='utf-8') as file:
        data = file.read()
    words= data.split(" ")
    startWords = [] #BOS
    endWords = [] #EOS
    ngrams = {} #Dictionary with words and followup words.

    for index in range(0, len(words)-1):
        if checkValidWord(words[index]) and checkValidWord(words[index+1]): #Check if it is a "real" word.
            if len(words[index]) > 0 and words[index][0].isupper(): #Add BOS words
                startWords.append(words[index])
            if checkEndWord(words[index]): #Add EOS words
                endWords.append(words[index])
            if words[index] in ngrams and index != len(words):
                ngrams[words[index]].append(words[index + 1])
            elif index != len(words):
                ngrams[words[index]] = [] #create new list
                ngrams[words[index]].append(words[index + 1])

    startWord = random.choice(startWords)
    output = startWord + " "
    for i in range(0,14):
        if(startWord in ngrams):
            newWord = random.choice(ngrams[startWord])
        else:
            newWord = random.choice(startWords)
        output += newWord + " "
        startWord = newWord
    output += random.choice(endWords)
    return output


