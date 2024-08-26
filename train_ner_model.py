import spacy
from spacy.training.example import Example
from spacy.util import compounding, minibatch


def find_entity_positions(text, entity_values):
    """
    Finds the start and end positions of given entity values in the text.

    :param text: The string in which to find the entities.
    :param entity_values: A list of strings representing the entities (e.g., materials, colors) to find.
    :return: A list of tuples with (start_index, end_index, entity_value).
    """
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
    """
    Creates the TRAIN_DATA format for NER training.

    :param texts_and_entities: List of tuples with text and the entities to find.
    :return: Formatted TRAIN_DATA with entity positions.
    """
    train_data = []

    for text, entity_values in texts_and_entities:
        entity_positions = find_entity_positions(text, entity_values)
        formatted_entities = [
            (start, end, "MATERIAL" if entity.isdigit() else "COLOR")
            for start, end, entity in entity_positions
        ]
        train_data.append((text, {"entities": formatted_entities}))

    return train_data


# Define your texts and entities
texts_and_entities = [
    ("Can you set material 1234 and 4567 color to Red?", ["1234", "4567", "Red"]),
    ("Please update material 2345 color to Blue.", ["2345", "Blue"]),
    (
        "Set material 6789 to Green and 9876 to Yellow.",
        ["6789", "9876", "Green", "Yellow"],
    ),
    ("Material 1111 and 2222 should be changed to Black.", ["1111", "2222", "Black"]),
    ("Could you make material 3333 and 4444 color Orange?", ["3333", "4444", "Orange"]),
    ("Change material 5555 color to Pink.", ["5555", "Pink"]),
    ("I'd like material 6666 and 7777 set to Purple.", ["6666", "7777", "Purple"]),
    ("Switch material 8888 and 9999 to Cyan.", ["8888", "9999", "Cyan"]),
    ("Assign material 1234 the color Brown.", ["1234", "Brown"]),
    (
        "The color for material 2345 and 3456 should be White.",
        ["2345", "3456", "White"],
    ),
    ("Make material 4567 and 5678 color to Gray.", ["4567", "5678", "Gray"]),
    ("Material 6789 needs to be set to Magenta.", ["6789", "Magenta"]),
    ("Could you please change material 7890 to the color Yellow?", ["7890", "Yellow"]),
    ("Update material 8901 color to Orange.", ["8901", "Orange"]),
    (
        "The materials 9012 and 0123 should both be set to Blue.",
        ["9012", "0123", "Blue"],
    ),
    ("Apply the color Red to material 1234 and 5678.", ["Red", "1234", "5678"]),
    ("Set materials 2345 and 6789 to the color Black.", ["2345", "6789", "Black"]),
    (
        "Material 3456 and 7890 should be assigned the color White.",
        ["3456", "7890", "White"],
    ),
    ("Can you change the color of material 4567 to Green?", ["4567", "Green"]),
    (
        "Please set the color of materials 5678 and 8901 to Pink.",
        ["5678", "8901", "Pink"],
    ),
    (
        "I'd like to update material 6789 and 0123 with the color Cyan.",
        ["6789", "0123", "Cyan"],
    ),
    ("Adjust the material 7890 to have the color Purple.", ["7890", "Purple"]),
    (
        "Please assign material 8901 and 2345 the color Brown.",
        ["8901", "2345", "Brown"],
    ),
    ("Material 3456 color should be set to Yellow.", ["3456", "Yellow"]),
    ("Set the material 4567 and 6789 colors to Magenta.", ["4567", "6789", "Magenta"]),
    ("Material 5678 needs its color changed to Red.", ["5678", "Red"]),
    ("Make the material 6789 and 7890 color to Blue.", ["6789", "7890", "Blue"]),
    ("Please set material 8901 and 0123 color to Orange.", ["8901", "0123", "Orange"]),
    ("I need material 1234 and 2345 to be colored Gray.", ["1234", "2345", "Gray"]),
    (
        "Update the color for material 3456 and 4567 to White.",
        ["3456", "4567", "White"],
    ),
    (
        "Can you set material 13347 blue and 6789 pink?",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Update material 13347 to blue and 6789 to pink.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Assign blue color to material 13347 and pink to material 6789.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Could you change material 13347 to blue and material 6789 to pink?",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Please set the color of material 13347 to blue, and update material 6789 to pink as well.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Material 13347 should be changed to blue, while material 6789 needs to be pink.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "The color blue should be applied to material 13347, and pink to material 6789.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Set material 13347 with the color blue and material 6789 with pink.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "For material 13347, use blue; for material 6789, use pink.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Change the color of 13347 to blue and switch 6789 to pink.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "In the new batch, material 13347 needs to be blue, and 6789 should be pink. Please update accordingly.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Can you ensure material 13347 is colored blue and that 6789 gets pink? Also, remember to mark them correctly.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Assign blue to material 13347, pink to 6789, and red to material 1234.",
        ["13347", "blue", "6789", "pink", "1234", "red"],
    ),
    (
        "Material 13347 should be updated to blue, material 6789 should be pink, and make sure they match the color scheme.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "First, set material 13347 to blue, then change material 6789 to pink, and finally review the colors.",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Material 13347: update to blue; material 6789: change to pink!",
        ["13347", "blue", "6789", "pink"],
    ),
    (
        "Could you confirm that material 13347 will be blue and material 6789 will be pink? Thanks.",
        ["13347", "blue", "6789", "pink"],
    ),
]

# Generate the TRAIN_DATA
TRAIN_DATA = create_train_data(texts_and_entities)

# Load a blank English model
nlp = spacy.blank("en")

# Create a new NER pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Add new labels to the NER
ner.add_label("MATERIAL")
ner.add_label("COLOR")

# Disable other pipelines during training
pipe_exceptions = ["ner"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

# Start the training
with nlp.disable_pipes(*unaffected_pipes):
    optimizer = nlp.begin_training()
    for i in range(100):  # Number of iterations
        losses = {}
        # Create batches of training data
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], drop=0.5, losses=losses)
        print(f"Iteration {i + 1}, Losses: {losses}")

# Save the trained model
nlp.to_disk("my_ner_model")

# Test the model with a new text
test_text = "set material 13347 to blue  material 6789 to pink."
doc = nlp(test_text)

# Print the tokens
print(f"Tokens: {[token.text for token in doc]}")

# Print the recognized entities and their labels
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
