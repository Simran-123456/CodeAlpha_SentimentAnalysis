from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# Sample reviews
reviews = [
    "This product is amazing!",
    "Worst experience ever.",
    "The product is okay.",
    "I really loved it.",
    "Not good at all."
]

# Analyze sentiment
results = []

for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append([review, sentiment])

# Create DataFrame
df = pd.DataFrame(results, columns=["Review", "Sentiment"])

# Print results
print(df)

# Visualization
df['Sentiment'].value_counts().plot(kind='bar')

plt.title("Sentiment Analysis Results")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.savefig("sentiment_chart.png")
plt.show()

print("Sentiment Analysis Completed!")