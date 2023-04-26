
import nltk

# download the stop words list (only needed once)
nltk.download('stopwords')

# import the stop words list
stop_words = nltk.corpus.stopwords.words('english')

print(stop_words)
class TextCleaner:


    def __init__(self) -> None:
        pass