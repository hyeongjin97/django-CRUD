sentence = "    안녕하세요 저는 전형진 입니다 안녕하세요"
wordList = sentence.split()
delete = sentence.replace(" ","")

wordDict = {}
   
for word in wordList:
    if word in wordDict:
                wordDict[word] += 1
    else:
            wordDict[word] = 1
wordDict_items = wordDict.items()

print(delete)

