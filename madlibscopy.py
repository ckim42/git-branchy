# Took code from my Mad Libs assignment from CS 1.1

def getPronounInput():
    return input("Enter a pronoun: ")

def getNounInput():
    return input("Enter a noun: ").lower()

def getVerbInput():
    return input("Enter a verb in the past tense: ").lower()

def getAdverbInput():
    return input("Enter an adverb: ").lower()

def getAdjInput():
    return input("Enter an adjective: ").lower()

def getWordInput(type):
    if (type == "noun"):
        return getNounInput()
    if (type == "adverb"):
        return getAdverbInput()
    if (type == "verb"):
        return getVerbInput()
    if (type == "adj"):
        return getAdjInput()
    if (type == "pronoun"):
        return getPronounInput()

lib = '''%s felt fabulous. You might have heard of them - they're a rich and famous celebrity. They walked into the %s coffeeshop and bought a pricey %s. The paparazzi followed %s. They %s the celebrity without being spotted. It made headlines the next day!'''
words = []
wordsNeeded = ["pronoun", "adj", "noun", "adverb", "verb"]
for x in wordsNeeded:
    words.append(getWordInput(x))

lib = lib % tuple(words)

print (lib)
