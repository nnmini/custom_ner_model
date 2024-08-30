""

import spacy

# import loadIntent from prepareData.py
from prepareData import loadIntents
from spacy.training.example import Example
from spacy.util import compounding, minibatch


def find_entity_positions(text, entity_values):
    entities = []
    for entity_value in entity_values:
        start_index = text.find(entity_value)
        if start_index != -1:
            end_index = start_index + len(entity_value)
            entities.append((start_index, end_index, entity_value))
        else:
            print(f"Entity '{entity_value}' not found in the text.")
    return entities


def create_train_data(texts_and_entities):
    train_data = []
    for text, entity_values in texts_and_entities:
        entity_positions = find_entity_positions(text, entity_values)
        formatted_entities = [
            (start, end, "MATERIAL" if entity.isdigit() else "COLOR")
            for start, end, entity in entity_positions
        ]
        train_data.append((text, {"entities": formatted_entities}))
    return train_data


def load_intents_from_file(filename):
    texts_and_entities = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",[")
            text = parts[0].strip()
            entity_list_str = "[" + parts[1].strip()
            entities = ast.literal_eval(entity_list_str)
            texts_and_entities.append((text, entities))
    return texts_and_entities


texts_and_entities = loadIntents()
TRAIN_DATA = create_train_data(texts_and_entities)

nlp = spacy.blank("en")

# Check current pipeline components
print(f"Initial pipeline components: {nlp.pipe_names}")

# Create a new NER pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Add new labels to the NER
ner.add_label("MATERIAL")
ner.add_label("COLOR")

# Print the updated pipeline components
print(f"Updated pipeline components: {nlp.pipe_names}")

# Disable other pipelines during training
pipe_exceptions = ["ner"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
print(f"Disabled pipes: {unaffected_pipes}")

# Start the training
with nlp.disable_pipes(*unaffected_pipes):
    optimizer = nlp.begin_training()
    for i in range(100):  # Number of iterations
        losses = {}
        # Create smaller batches to handle large data
        batches = minibatch(
            TRAIN_DATA, size=compounding(2.0, 16.0, 1.001)
        )  # Adjust batch size as needed
        for batch in batches:
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], drop=0.5, losses=losses)
        print(f"Iteration {i + 1}, Losses: {losses}")

# Save the trained model
nlp.to_disk("my_ner_model")

# Test the model with a new text
test_text = "Introduce MTLC SILVER GREY-03530 to the 1234."
doc = nlp(test_text)

# Print the tokens
print(f"Tokens: {[token.text for token in doc]}")

# Print the recognized entities and their labels
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
