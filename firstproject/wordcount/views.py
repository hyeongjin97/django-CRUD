from os import replace
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def result(request):
    sentence = request.GET['sentence']
    wordList = sentence.split()
    wordDict = {}
    all_exceptCount = sentence.replace(" ","")
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return render(request,'result.html',
        {'fulltext':sentence, 'sentence_count':len(wordList),
        'word_count':wordDict.items,'all_count':len(sentence),
        'all_exceptCount':len(all_exceptCount)
        })


# Create your views here.
