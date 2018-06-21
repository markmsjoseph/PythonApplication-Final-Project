# i used list comprehensions, map and filter in this class, i commented where i used them
from nltk import word_tokenize
import nltk as nltk


# creates a sentence object with parts of speech attached to each word so you can look up the POS for each word or
# search for nouns or verbs
class SentencePartOfSpeechTagger:

    def __init__(self, sentenctToTokenize):

        self.sentenctToTokenize = sentenctToTokenize
        # split up the sentence and store it in text
        text = word_tokenize(sentenctToTokenize)
        # use nltk library to get the parts of speech of the sentence
        self.words = nltk.pos_tag(text)

    # get the entire sentence and all of its parts of speech
    def getPartsOfSpeech(self):
        [print(word + ": " + POS) for word,POS in self.words]



    # use of simple word comprehension
    def getProperNouns(self):
        #list comprehension usage
        var = [word.upper() for word,POS in self.words if POS =="NNP" or POS =="NNPS" ]

        # list comprehension returns a new list with the proper nouns in capital letters
        if len(var) == 0:
            print("There are no Proper Nouns")
        else:
            print("\nProper Nouns:")
            for i in range(len(var)):
                print(var[i])



    # use of map
    def getVerbs(self):

        # callback function for map
        def printPos(word):
            string ="Verb: "
            string =string + word
            return string

        var = [word for word,POS in self.words if POS =="VB" or POS =="VBD" or POS =="VBG" or POS =="VBN" or POS =="VBP" or POS =="VBZ"]

        if len(var) == 0:
            print("There are no verbs")
        else:
            # call map which takes the pringPOS function. map returns iterable object so just loop over and print
            for item in map(printPos,var):
                print(item)



    # use of filter
    def getNouns(self):

        # function to be used in filter
        def isNounType(POS):
            if POS[1] =="NN" or POS[1] =="NNS" or POS[1] =="NNP" or POS[1] =="NNPS":
                return True
            else:
                return False

        # for every word in the sentence, check if it is a type of noun and store it in a list
        var = list(filter(isNounType, self.words))

        # if the list is empty
        if len(var) == 0:
            print("There are no nouns")
        # print the list with a nice format
        else:
             print("\nNouns:")
             [print(word + ": " + POS) for word,POS in var]




    # use nltk's build in function that displays all parts of speech in their penn
    # treebank(penn treebank is a list of POS, there are other treebanks but penn is popular and most useful)
    # this shows the part of speech followed by examples of its usage
    def getListOfPartsOfSPeech(self):
       nltk.help.upenn_tagset()





    # search for a unknown part of speech(parts of speech that i did not explicitly list as noun, verb or proper noun) in the penn treebank
    def searchForPartOfSpeech(self, POS):
        file = open('words.txt', 'r')
        var = [print(line) for line in file if str(POS) + ":" in line]
        if len(var) == 0:
            print("Unknown Part of speech, enter pos such as NN, NNP etc")
        else:
            [print(line) for line in file if str(POS) + ":" in line]




running = True
response = input("Enter your sentence \n")
sentence = SentencePartOfSpeechTagger(response)
print("What do you want to do with it? \nEnter GN for getting the nouns\nEnter GV for getting verbs\nEnter GPN for getting the proper nouns\n"
                  "Enter SEARCH to search for a part of speech eg NN to search for its definition\nEnter GL to get a list of all parts of speech and their description\n")
sentence.getPartsOfSpeech()

while running:
    print("\nEnter GN for getting the nouns\nEnter GV for getting verbs\nEnter GPN for getting the proper nouns\nEnter SEARCH "
          "to search for a part of speech eg NN to search for its definition\nEnter GL to get a list of all parts of speech and their description\n")

    reply = input("")

    if reply == "GN":
        sentence.getNouns()
    elif reply == "GV":
        sentence.getVerbs()
    elif reply == "GPN":
        sentence.getProperNouns()
    elif reply == "GL":
        sentence.getListOfPartsOfSPeech()
    elif reply == "SEARCH":
        pos = input("Enter your pos eg NN or VBZ etc\n")
        sentence.searchForPartOfSpeech(pos)
    elif reply == "quit":
        running = False


print('DONE')
