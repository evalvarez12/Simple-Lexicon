
symbols = [",", ".", ";", ":", "'", '"',"`", "(", ")", '/', "&","?", "!","*","<",">","\r","\t"]
#TO DO add space recognition eiter tab or space


def processFile(filename) :
    with open(filename, 'r') as data :
        return processText(data.read())
    #except EnvironmentError : 
        #print "ERROR: Can't load file"
        #return None
  
def processText(data) :
    lines = data.split("\n")
    processed_lines = []
    for i in lines :
        processed_lines += processLine(i)    
    return processed_lines  
  
def processLine(data) :
    words = data.split(" ")
    processed_words = []
    for i in words :
        processed_words += processWord(i)    
    return processed_words



def processWord(word) :
    if word.count("-") :
        extra_words = word.split("-")
        words = []
        for i in extra_words :
            words += processWord(i)
        return words
    else :
        for sym in symbols :
            word = word.replace(sym,"")
        if word == "" :
            return []
        else :
            word = word.lower()  
            if word.isdigit() :
	        word = "#"  
            return [word]