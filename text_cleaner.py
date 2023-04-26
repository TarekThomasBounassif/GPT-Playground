
import nltk
from nltk.stem import PorterStemmer

class TextCleaner:

    def __init__(self) -> None:
        nltk.download('stopwords')
        self.stop_words = nltk.corpus.stopwords.words('english')
        self.stemmer = PorterStemmer()

    def remove_stop_words_string(self, str_in:str) -> str:
        for s_word in self.stop_words:
            str_in = str_in.replace(s_word, '')
        return str_in
    
    def tokenize(self, str_in:str) -> list:
        str_in = str_in.replace('\n', '').replace('\t', '')
        tokens = str_in.split()
        tokens = [token for token in tokens if len(token) > 1]
        tokens = [token.lower() for token in tokens]
        tokens = [token for token in tokens if token not in self.stop_words]
        #tokens = [self.stemmer.stem(token) for token in tokens]
        return tokens