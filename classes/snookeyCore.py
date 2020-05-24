# snookey stream subreddit streamName
import webbrowser

class snookeyCore:
    #apiPublicKey is also ClientID
    apiPublicKey = "uSqdqXc1RK3fcw"

    def __init__(self):
        self.command = None
        self.subreddit = None
        self.streamName = None

    def generateAccessTokenLink(self):
        #RedditOnAndroid
        client_id = "ohXpoqrZYub1kg"
        response_type = "token"
        scope = "*"
        callback = "http://localhost:65010/callback"
        state = "SNOOKEY"
        request_url = "https://www.reddit.com/api/v1/authorize?client_id=%s&response_type=%s&redirect_uri=%s&scope=%s&state=%s" % (client_id, response_type, callback, scope, state)

        #Open browser to get access token
        webbrowser.open(request_url, new=0)
