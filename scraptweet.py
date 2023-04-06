import tweepy
import gspread
from oauth2client.service_account import ServiceAccountCredentials



# Define your Twitter API credentials
consumer_key = 'g23Gz7IHKdEWmBg9dvU4jDXXj'
consumer_secret = 'kxpeO2qpcKqnyyyXir7VX3Fdi6sWxIIzAvWHZ8xaFbs1DlZuJM'
access_token = '713689895907143681-z7CGsDnYzJiAirjdZrbdO0NdV51ElDP'
access_token_secret = 'Bb9Yn9dSkKtxHUdOB3AXE7iZhDw0Q3UHoKBSOzK82zm6T'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Authenticate with the Google Sheets API
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Kurnool Ramesh\\Desktop\\VS Code\\assignment Vscale\\file.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Your Google Sheet Name').worksheet('Input')

# Get the list of tweets from the first column of the Input worksheet
tweets = sheet.col_values(1)

# Scrape text from each tweet and save to the Output worksheet
output_sheet = client.open('Your Google Sheet Name').worksheet('Output')
for tweet in tweets:
    try:
        tweet_obj = api.get_status(tweet, tweet_mode='extended')
        text = tweet_obj.full_text
        output_sheet.append_row([text])
    except Exception as e:
        print(f"Error scraping tweet {tweet}: {e}")