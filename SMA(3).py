#3
import pandas as pd
from textblob import TextBlob

data = {
    'date': pd.to_datetime(['2023-11-18', '2023-11-18', '2023-11-19', '2023-11-19', '2023-11-20', '2023-11-20']),
    'text': [
        "aditya Corp's new farm is amazing!",
        "I'm having trouble with adi Corp's customer service.",
        "Adi Corp is the best!",
        "Adi Corp's prices are too high.",
        "I love Adi farm!",
        "Adi Corp is a terrible company."
    ]
}

df = pd.DataFrame(data)

df['sentiment'] = df['text'].apply(lambda text: TextBlob(text).sentiment.polarity)
average_sentiment = df['sentiment'].mean()
overall_sentiment = "Positive" if average_sentiment > 0 else "Negative" if average_sentiment < 0 else "Neutral"
sentiment_by_date = df.groupby('date')['sentiment'].mean().reset_index()

print(df)
print(f"Overall Sentiment: {overall_sentiment}")
print(sentiment_by_date)