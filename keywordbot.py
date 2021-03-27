import praw
import time
import Build_Email

#Change keywords as desired
KEYWORDS = [ '1080', '1080ti', '1080 ti', '5600XT', '5600 XT', 'Vega', 'Vega 64', 'Vega64', 'Vega 56', 'Vega56',
             '1660', '1660 super', '580', '5700xt', '5700 xt', '5700', '3060']

#Makes sure seller is willing to ship item.
#Replace with 'Trade' if trade is desired
#Replace with 'local','cash' if local sale is desired.
KEYWORD2 = ['paypal']

SUBREDDIT = 'hardwareswap'

MESSAGE_SUBJECT = 'Found new post '

MESSAGE_BODY = 'Link to post: '

def connect_to_reddit():
    reddit = praw.Reddit(
    username = 'Reddit Username',
    password = 'Reddit Password',
    client_id = 'Client Id provided by Reddit',
    client_secret = 'Client Secret provided by Reddit',
    user_agent = 'what it is, who made it')
    return reddit

# Main program. Don't mess with anything below here unless you know what you're doing.
def send_message(submission, keyword):
    try:
        print(submission.shortlink)
        print(submission.title)
        Build_Email.send_email(MESSAGE_SUBJECT+str(keyword), MESSAGE_BODY+str(submission.shortlink))
    except Exception as e:
        print(e)
        time.sleep(60)

def find_submissions():
    try:
        while True:
            for submission in reddit.subreddit(SUBREDDIT).stream.submissions():
                for keyword in KEYWORDS:
                    try:
                        title = submission.title.lower().split('[')
                        print(title[2])
                        print(keyword)
                        if keyword.lower() in title[2] and submission.created_utc > start_time:
                            try:
                                if 'paypal' in title[3]:
                                    send_message(submission, keyword)
                                    break
                            except Exception as e:
                                send_message(submission, keyword)
                                break
                    except Exception as e:
                        print(submission.title.lower())
                        print(keyword)
                        if keyword.lower() in submission.title.lower() and submission.created_utc > start_time:
                            send_message(submission, keyword)
                            break
    except Exception as e:
        print(e)
        time.sleep(60)

if __name__ == '__main__':
    start_time = time.time()
    reddit = connect_to_reddit()
    find_submissions()
