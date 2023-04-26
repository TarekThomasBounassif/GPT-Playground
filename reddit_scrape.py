import praw
from reddit_api_keys import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, USER_AGENT

class reddit_scrape:

    def __init__(self, subreddit:str) -> None:
        
        self.reddit_crawler = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URL,
            user_agent=USER_AGENT
        )

        self.subreddit_obj = self.reddit_crawler.subreddit(subreddit)
        self.subreddit = subreddit

    def get_posts(self, count:int):
        return self.subreddit_obj.new(limit=count)

    
