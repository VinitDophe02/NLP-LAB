# Importing the required libraries from spaCy
import spacy
from spacy import displacy

# Load the small English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Input text: A descriptive paragraph about Turkey and its geographical position
doc = nlp("Turkey is a transcontinental country that shares its land boundaries with eight countries—to the northwest with Greece and Bulgaria, to the northeast with Georgia, to the east with Armenia, Azerbaijan’s Nakhchivan exclave, and Iran, and to the south with Iraq and Syria. In terms of seas, Turkey is uniquely positioned, bordered by the Black Sea to the north, the Aegean Sea to the west, and the Mediterranean Sea to the south, while the Sea of Marmara and the Turkish Straits (the Bosporus and Dardanelles) connect these seas and separate its European and Asian parts.")

# Iterate through the named entities detected in the text
for ent in doc.ents:
    # Print entity text, start position, end position, and entity label
    # Format ensures proper alignment of the output
    print(f"{ent.text:<25} {ent.start_char:<5} {ent.end_char:<5} {ent.label_}")

# Visualize the named entities using spaCy's displaCy visualizer
# This will start a local server and open the visualization in a browser
displacy.serve(doc, style="ent")
