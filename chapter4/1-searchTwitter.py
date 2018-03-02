from twitter import Twitter, OAuth

token = '813962685096173568-ij4CRLexOG8AOAu5GkweDnnmMksfwvI'
token_secret = 'Nil3tT1nnxY3kDnJLfZ1vTiDeFBmzkqNcyPHWpHbujbkn'
consumer_key = '28bRGP3m3caQNnytHUKiUnQVE'
consumer_secret = 'JXf21TFtxOm4IAdErKdu5AHSzjd4jYuwy0GhSmXENMBZP3zJzG'
# token, token_secret, consumer_key, consumer_secret
t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
tweets = t.statuses.update(status='Hello,world')
# tweets = t.search.tweets(q='#java')
print(tweets)
