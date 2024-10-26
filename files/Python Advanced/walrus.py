def get_info(text:str)->dict:
    return {
        "text": (sentense := text),
        "length": (characterLen := len(text.replace(" ",""))),
        "words": (words:=text.split()),
        "wordsCount":(wordsCount := len(words)),
        "avg_word_len": round(characterLen/wordsCount,2)
    }

if __name__=="__main__":
    # print(get_info("Lets get line info"))
    for key,value in get_info("Lets get line info").items():
        print(key,value,sep=" : ")