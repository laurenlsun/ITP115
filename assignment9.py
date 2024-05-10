# Lauren Sun, sunlaure@usc.edu
# ITP 115, Fall 2022
# Section: 31814
# Assignment 9
# Description: asks the user for a language,
# then translates some english words of the user's choice into that language. saves to a txt file


def readFileForLanguages(filenameStr):
    fileRead = open(filenameStr, 'r')
    header = fileRead.readline() # read header
    header = header.strip()
    langList = header.rsplit(',') # create list of items in header (languages)
    fileRead.close()
    return langList

def getLanguageFromUser(languagesList):
    print("Translate English words to one of the following languages:")
    noEnglishList = [] # just a list of languages without english
    for lang in languagesList:
        if lang != "English":
            noEnglishList.append(lang) # add language name to the list if it's not english
    print(noEnglishList)
    invalid = True # boolean variable to determine whether or not the language entered is valid
    while invalid:
        userLangChoice = (input("Enter a language: ")).capitalize()
        if userLangChoice not in noEnglishList:
            print(userLangChoice, "is not a valid language.")
        else: # the language entered is valid
            invalid = False # exit loop
    print("You have entered", userLangChoice)
    return userLangChoice


def readFileForWords(filenameStr, languagesList, languageStr):
    wordsList = [] # list containing words in the language
    fileIn = open(filenameStr, "r")
    fileIn.readline() # remove first line
    index = languagesList.index(languageStr) # index of where the language is located in the list. should be the same index as corresponding words in this language in each line
    for line in fileIn:
        line = line.strip()
        list = line.split(",")
        wordsList.append(list[index]) # add words to wordsList one by one
    fileIn.close()
    return wordsList


def createFileWithTranslations(languageStr, englishList, langList):
    fileWrite = open(languageStr + ".txt", "w") # create new file with language as name
    line = "Words translated from English to " + languageStr
    print(line, file=fileWrite) # writes header into text file
    cont = True # boolean variable to determine whether or not the user wants to continue entering words to translate
    while cont:
        word = input("Enter a word to translate (return to quit): ")
        if word in englishList: # word is available for translation in english list
            translation = langList[englishList.index(word)] # find corresponding word in that line in the chosen language
            if translation != "-": # translation in chosen language actually available
                print(word, "is translated to", translation) # print confirmation
                print(word, " -> ", translation, file=fileWrite) # write line into txt file
            else: # if it says "-" instead of having a translation
                print(word, "does not have a translation.")
        if word not in englishList and word != "": # word isn't in english list, but stay in the loop
            print(word, "is not in the English list.")
        if word == "": # user wants to quit
            cont = False # exit loop
    fileWrite.close()
    print("Translated words have been saved to", languageStr + ".txt.")


def main():
    print("Language Translator")
    fileName = "languages.csv"
    listOfLangs = readFileForLanguages(fileName) # list of languages
    lang = getLanguageFromUser(listOfLangs) # language chosen by user to translate english words into
    englishList = readFileForWords(fileName, listOfLangs, "English") # create list containing english words
    langList = readFileForWords(fileName, listOfLangs, lang) # create list containing words in chosen language
    createFileWithTranslations(lang, englishList, langList) # writes translations into text file by matching language index with word index in word's row

main()