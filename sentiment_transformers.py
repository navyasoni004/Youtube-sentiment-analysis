from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_transformer(text):
    result = classifier(text[:512])[0]
    return result['label'], result['score']