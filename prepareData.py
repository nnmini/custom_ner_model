import random
intents_with_material_color = [
    "Introduce {code} to the {material}.",
    "Change the color of {material} to {code}.",
    "Assign color {code} to {material}.",
    "Apply a shade of {code} to {material}.",
    "Add a tint of {code} to {material}.",
    "Can you set material {material} color to {code}",
    "Please update material {material} color to {code}",
    "Set material {material} to {code}.",
    "Material {material} should be changed to {code}.",
    "Could you make material {material} color {code}?",
    "I'd like material {material} set to {code}.",
    "Switch material {material} to {code}.",
    "Assign material {material} the color {code}.",
    "The color for material {material} should be {code}.",
    "Make material {material} color to {code}.",
    "Material {material} needs to be set to {code}.",
    "Could you please change material {material} to the color {code}?",
    "Update material {material} color to {code}.",
    "The materials {material} should both be set to {code}.",
    "Apply the color {code} to material {material}.",
    "Set materials {material} to the color {code}.",
    "Material {material} should be assigned the color {code}.",
    "Can you change the color of material {material} to {code}?",
    "Please set the color of materials {material} to {code}.",
    "I'd like to update material {material} with the color {code}.",
    "Adjust the material {material} to have the color {code}.",
    "Please assign material {material} the color {code}.",
    "Material {material} color should be set to {code}.",
    "Set the material {material} colors to {code}.",
    "Material {material} needs its color changed to {code}.",
    "Make the material {material} color to {code}.",
    "Please set material {material} color to {code}.",
    "I need material {material} to be colored {code}.",
    "Update the color for material {material} to {code}.",
    "Can you set material {material} {code}?",
    "Update material {material} to {code}.",
    "Assign {code} to material {material}.",
    "Could you change material {material} to {code}",
    "Please set the color of material {material} to {code}",
    "Material {material} should be changed to {code}",
    "The color {code} should be applied to material {material}",
    "Set material {material} with the color {code}",
    "For material {material}, use {code}",
    "Change the color of {material} to {code}",
    "In the new batch, material {material} needs to be {code}",
    "Can you ensure material {material} is colored {code}",
    "Assign {code} to material {material}",
    "Material {material} should be updated to {code}",
    "First, set material {material} to {code}",
    "Could you confirm that material {material} will be {code}? Thanks.",
    "Can you set material {material} and color to {code}?",
    "Update material {material} to {code}.",
    "Assign {code} to material {material}",
    "Could you change material {material} to {code}",
    "Please set the color of material {material} to {code}",
    "Can you find the combination of material {material}with color {code}?",
    "Can you find color {code} and material {material}?",
    "find material {material} with color {code}.",
    "Can you find material {material} with color {code}?",
    "find material and {material} with color {code}.",
    "Can you find material {material} with color {code}?"
    
    
]
materials = ["1234", "5678", "56745"]  # Replace with your actual materials
color_codes = ["00A",
"00B",
"00C",
"00D",
"00E",
"00F",
"00G",
"00H",
"00I",
"00J",
"00K",
"00L",
"00M",
"00N",
"00P",
"00Q",
"00R",
"00S",
"00T",
"00U",
"00V",
"00W",
"00X",
"00Y",
"00Z",
"01A",
"01B",
"01C",
"01D",
"01E",
"01F",
"01G",
"01H",
"01I",
"01J",
"01K",
"01L",
"01M",
"01N",
"01P",
"01Q",
"01R",
"01S",
"01T",
"01U",
"01V",
"01W",
"01X",
"01Y",
"01Z",
"02A",
"02B",
"02C",
"02D"] 
 # Replace with your actual color codes
 # define function that return templates
def loadIntents():
    templates = []
    for intent in intents_with_material_color:
        # select random material and color code
        material = random.choice(materials)
        code = random.choice(color_codes)
        filled_intent = intent.format(material=material, code=code)
        templates.append((filled_intent, [code, material]))
        print(filled_intent)
    with open("templates.txt", "w") as file:
        for template in templates:
            file.write(str(template))
            file.write("\n")
    return templates
def getIntents():
    templates = []
    for intent in intents_with_material_color:
        # select random material and color code
        material = random.choice(materials)
        code = random.choice(color_codes)
        filled_intent = intent.format(material=material, code=code)
        templates.append(filled_intent)
        print(filled_intent)
    with open("templates.txt", "w") as file:
        for template in templates:
            file.write(str(template) + "\n")
    return templates

# call loadIntents function
getIntents()
