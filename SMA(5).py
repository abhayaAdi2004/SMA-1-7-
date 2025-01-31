#5
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample list of tweets
tweets = ["This is a great day!", "I love programming in Python.", "Data science is amazing.", "Python is versatile."]

# Combine all tweets into a single string
text = " ".join(tweet for tweet in tweets)

# Generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the generated image
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()