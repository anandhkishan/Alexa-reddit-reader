from flask import Flask
from flask_ask import Ask,statement, question, session
import json
import time
import requests
import unidecode

app = Flask(__name__)
ask = Ask(app,"/reddit_reader")

def get_headlines():
    user_pass_dict = {'user':'[REDDIT_USERNAME]','passwd':'[REDDIT_PASSWORD]','api_type':'json'}
    sess = requests.Session()
    #this is needed by reddit incase to ratelimit if there are more  requests
    #from particular user-agent
    #explained here: https://youtu.be/oJ6MBvzgPcQ
    sess.headers.update({'User-Agent':'Fetching data for alexa'})
    sess.post('https://www.reddit.com/api/login',data= user_pass_dict)
    #sleeping here to avoid blocking/ratelimiting by reddit for more hits/sec
    time.sleep(1)
    url = "https://reddit.com/r/worldnews/.json?limit=5"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '...'.join([i for i in titles])
    return titles

#This is just to see in the browser
#not related to alexa skill
@app.route("/")
def homepage():
    return "hey ya! wassup dude?"

@ask.launch
def start_skills():
    welcome_message = "hello there! Would you like to get the worldnews from reddit? "
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = "{}".format(headlines)
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = "Im not sure why you called me then..but okay.. bye"
    return statement(bye_text)

if __name__ == "__main__":
    app.run(debug = True)

