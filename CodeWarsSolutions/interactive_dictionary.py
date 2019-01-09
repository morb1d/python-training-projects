class Dictionary():
    def __init__(self):
        self.dictionary={}

    def newentry(self, word, definition):
        self.dictionary[word]=definition
        
    def look(self, key):
        return print(self.dictionary.get(key,"Cant find entry for {}".format(key)))


d = Dictionary()
    
d.newentry("Apple", "A fruit")
d.look("Apple")
d.look("Banana")