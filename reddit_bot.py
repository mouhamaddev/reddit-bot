import praw

userAgent = "uAgent"

cID = config.client_id

cSC= config.client_secret

userN = config.username

userP = config.password

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('weather') 

bot_phrase = 'Aw shucks, looks like I am staying in >:(' 

keywords = {'Cold', 'chicago', 'polar', 'vortex'}

for submission in subreddit.hot(limit=10):

n_title = submission.title.lower() 

for i in keywords:

if i in n_title:

numFound = numFound + 1

print('Bot replying to: ')

print("Title: ", submission.title)

print("Text: ", submission.selftext)

print("Score: ", submission.score)

print("---------------------------------")

print('Bot saying: ', bot_phrase)

print()

submission.reply(bot_phrase)

if numFound == 0:

print()

print("Sorry, didn't find any posts with those keywords, try again!")
