# -*- coding: utf-8 -*-
"""SMA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S89Ems11oJmNGWvUnq6Wg-npOZ4G9XsH
"""

from instagrapi import Client

# Credentials
user = 'username'
password = 'password'

# Initialize client and login
cl = Client()
cl.login(user, password)

# Target Instagram account
instaID = 'cristiano'
user_id = cl.user_id_from_username(instaID)
medias = cl.user_medias(user_id, 20)
user_info = cl.user_info(user_id)

# Metrics
followers_count = user_info.follower_count
total_likes = sum(media.like_count for media in medias)
total_comments = sum(media.comment_count for media in medias)
total_posts = len(medias)

if total_posts > 0:
    avg_likes = total_likes / total_posts
    avg_comments = total_comments / total_posts
    total_engagement = total_likes + total_comments
    engagement_rate = (total_engagement / followers_count) * 100

    print(f"Account: {instaID}")
    print(f"Followers: {followers_count}")
    print(f"Total Posts Analyzed: {total_posts}")
    print(f"Average Likes: {avg_likes:.2f}")
    print(f"Average Comments: {avg_comments:.2f}")
    print(f"Engagement Rate: {engagement_rate:.2f}%")
else:
    print(f"No posts available for analysis for {instaID}.")