#2
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv("/content/synthetic_social_media_posts.csv")

def preprocess_text(text):

    if pd.isnull(text):
        return ""

    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    words = text.lower().split()

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return ' '.join(words)

df['cleaned_post'] = df['text'].apply(preprocess_text)

df.to_csv("cleaned_social_media_dataset.csv", index=False)

print(df.head())
