#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1244890776-wteM7XbRQxliqfmqgy7kB7zST6mkeprFM6CKfTy"
access_token_secret = "GPoP1iKLaaxlEgeab2QTMUYe7BzQ21YaqjklhXWGx1GoA"
consumer_key = "y0dQSPWpEqlfMk9gYeyeM4vpF"
consumer_secret = "CLPlkGRwAFSJK1b1YIhRFNOxsy3Onf3jHbmGaLub2KD5p6Zfo1"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])