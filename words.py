import collections


def addWordToDictionary(dict, word, meaning, mnemonic):
    word = word.lower()
    meaning = meaning
    mnemonic = mnemonic
    dict[word] = [meaning, mnemonic]


def displayWordMeaning(dict, word):
    word = word.lower()
    print("Word:\t\t" + word)
    print("Meaning:\t" + str(dict[word][0]))
    print("Mnemonic:\t" + str(dict[word][1]))


def addWordToFile(file, wordRow):
    with open(file, "a") as myfile:
        myfile.write(wordRow)


filename = 'wordList.txt'
f = open(filename, 'r')
dict = {}
for line in f:
    a = line.split('\t')
    addWordToDictionary(dict, str(a[0]), str(a[1]), str(a[2]))

menu = {'1': "Add Word.", '2': "Find Word", '3': "Edit Word", '4': "Practice", '5': "Exit"}

menu = collections.OrderedDict(sorted(menu.items()))

while True:
    options = menu.keys()
    for k, v in menu.items():
        print(k, v)
    selection = input("Please Select:")
    if selection == '1':
        wordToAdd = input("Word : ")
        wordMeaning = input("Meaning : ")
        wordMnemonic = input("Mnemonic : ")
        if wordToAdd in dict:
            print("Word already exists!")
        else:
            addWordToFile(filename, str(wordToAdd + str("\t") + wordMeaning + str("\t") + wordMnemonic + str("\n")))
            addWordToDictionary(dict, wordToAdd, wordMeaning, wordMnemonic)
            print(str("\nWord added!\n"))
            displayWordMeaning(dict, wordToAdd)
    elif selection == '2':
        wordToFind = input("Enter Word : ")
        displayWordMeaning(dict, wordToFind)
    elif selection == '3':
        print("Edit")
    elif selection == '4':
        print("Practice")
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")
