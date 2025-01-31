#4
import pandas as pd
import re

# Load the dataset
df = pd.read_csv("/content/tweets_dataset.csv")

def extract_hashtags(text):

    if pd.isnull(text):
        return []

    hashtags = re.findall(r"#\w+", text)
    return hashtags

df["hashtags"] = df["tweet"].apply(extract_hashtags)

df.to_csv("extracted_hashtags.csv", index=False)

print(df.head())