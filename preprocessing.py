import re

def clean_text(text):
    text = re.sub(r"http\S+", "", text)   # remove links
    text = re.sub(r"[^a-zA-Z ]", "", text)  # remove symbols
    return text.lower()