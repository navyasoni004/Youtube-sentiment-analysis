from youtube_api import extract_video_id, get_comments
from preprocessing import clean_text
from sentiment import analyze_sentiment
from collections import Counter
import matplotlib.pyplot as plt
from sentiment_transformers import analyze_transformer
from sentiment_textblob import analyze_textblob

url = input("Enter YouTube URL: ")

video_id = extract_video_id(url)
comments = get_comments(video_id)

#print("\nFirst 5 comments:\n")
#for c in comments[:5]:
#   print(c)
cleaned = [clean_text(c) for c in comments]

print("\nCleaned comments:\n")
for c in cleaned[:5]:
    print(c)

#print("lenth of comments is : ",len(comments))
#print("lenth of  cleaned comments is : ",len(cleaned))

scores = [analyze_sentiment(c) for c in cleaned]

print("\nSentiment Scores:\n")
for s in scores[:5]:
    print(s)

#converting scores to labels(positive / negative / neutral )
def classify(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"
    
#storing all these labels in a list and printing
labels = [classify(s) for s in scores]

#print("\nSentiment Labels:\n")
#for l in labels[:10]:
#   print(l)

# counting all the labels
result = Counter(labels)

print("\nFinal Sentiment Count:\n")
print(result)

# visualizing results through graphs
plt.pie(result.values(), labels=result.keys(), autopct='%1.1f%%')
plt.title("YouTube Comment Sentiment Analysis")
plt.show()

print("\nMODEL COMPARISON:\n")

for c in cleaned[:5]:
    vader_score = analyze_sentiment(c)
    tb_score = analyze_textblob(c)
    tr_label, tr_score = analyze_transformer(c)

    print("Text:", c)
    print("VADER:", vader_score)
    print("TextBlob:", tb_score)
    print("Transformer:", tr_label, tr_score)
    print("-"*50)