import spacy

nlp = spacy.load("my_ner_model")

test_text = "set material 13347 to blue  material 6789 to pink."
doc = nlp(test_text)

print(f"Tokens: {[token.text for token in doc]}")  # Check tokens

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
