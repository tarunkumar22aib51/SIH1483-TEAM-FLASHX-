import spacy 
nlp = spacy.load("en_core_web_lg")
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp("ElonMusk is owner of the Twitter Inc.")
print([(w.text, w.pos_) for w in doc])


