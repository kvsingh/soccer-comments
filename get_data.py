import praw, csv
import time
import pickle
import pprint

reddit = praw.Reddit(client_id='yourclientid',
                     client_secret='yourclientsecret',
                     user_agent='youruseragent')

subreddits = ["soccer", "liverpoolfc", "reddevils", "Gunners", "chelseafc"]
for subreddit_name in ['chelseafc', 'soccer', 'Gunners', 'reddevils', 'liverpoolfc']:
    subreddit = reddit.subreddit(subreddit_name)
    this_comments = []
    for submission in subreddit.top(time_filter='month', limit=100):
        submission.comments.replace_more(limit=0)
        comments = []
        for comment in submission.comments.list():
            id = comment.id
            comment_text = comment.body
            comments.append((id, comment_text))                 
        this_comments.extend(comments)

    pickle.dump(this_comments, open("reddit-top-1000-post-comments-" + subreddit_name + ".p", "wb"))
