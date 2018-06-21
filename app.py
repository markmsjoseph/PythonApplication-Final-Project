#NOTE this class is very similar to the one in partOfSpeechTagger.py but it does not contain map and filter and the other file does
# i also based this class off of hw 7. ie the webpage looks the same as hw 7's layout

from flask import Flask, render_template, request
from nltk import word_tokenize
import nltk as nltk

# from partOfSpeechTagger import *
app = Flask(__name__)
app.debug = True



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
        return [(word + ": " + POS) for word,POS in self.words]


    def getProperNouns(self):
        var = [word for word,POS in self.words if POS =="NNP" or POS =="NNPS" ]

        if len(var) == 0:
            print("There are no Proper Nouns")
        else:
            print("\nProper Nouns:")
            [print(word + ": " + POS) for word,POS in self.words if POS =="NNP" or POS =="NNPS" ]


    def getVerbs(self):
        var = [word for word,POS in self.words if POS =="VB" or POS =="VBD" or POS =="VBG" or POS =="VBN" or POS =="VBP" or POS =="VBZ"]

        if len(var) == 0:
            print("There are no verbs")
        else:
            print("\nVerbs:")
            [print(word + ": " + POS) for word,POS in self.words if POS =="VB" or POS =="VBD" or POS =="VBG" or POS =="VBN" or POS =="VBP" or POS =="VBZ"]


    def getNouns(self):

        var = [word for word,POS in self.words if POS =="NN" or POS =="NNS" or POS =="NNP" or POS =="NNPS" ]

        if len(var) == 0:
            print("There are no nouns")
        else:
            print("\nNouns:")
            [print(word + ": " + POS) for word,POS in self.words if POS =="NN" or POS =="NNS" or POS =="NNP" or POS =="NNPS" ]

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
    def __str__(self):
        return str(self.sentenctToTokenize)




@app.route('/', methods=['POST','GET'])
def home():

     if request.method == 'POST':
        sentence = SentencePartOfSpeechTagger(request.form['sentence'])
        POS = sentence.getPartsOfSpeech()

        return render_template('index.html', sentences = sentence, pos = POS)

     elif request.method == 'GET':
        return render_template('index.html')




@app.route('/getAllPartsOfSpeech', methods=['POST','GET'])
def projects_add():
    if request.method == 'POST':
        file = open('words.txt', 'r')

        return render_template('getAllPartsOfSpeech.html', file = file)

    elif request.method == 'GET':
        return render_template('getAllPartsOfSpeech.html')



@app.route('/searchForPartOfSpeech', methods=['POST','GET'])
def reports():
    sent = []
    if request.method == 'POST':
        file = open('words.txt', 'r')
        for line in file:
            if request.form['sentence'] in line:
                sent.append(line)

        if len(sent) == 0:
            sentences = ["Unknown Part of speech, enter pos such as NN, NNP etc"]
        else:
            sentences = sent
        return render_template('searchForPartOfSpeech.html', sentences=sentences)

    elif request.method == 'GET':
        return render_template('searchForPartOfSpeech.html')


app.run()
