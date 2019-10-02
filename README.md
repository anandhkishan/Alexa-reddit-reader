# Alexa-reddit-reader
Python script to make alexa develop a new skill and make it read to you the world news headlines from worldnews subreddit.

## Python Packages Used:
- [Flask](https://pypi.org/project/Flask/)
- [flask_asl](https://pypi.org/project/Flask-Ask/)
- [requests](https://pypi.org/project/requests/)
- [unidecode](https://pypi.org/project/Unidecode/)

## Requirements:
 - Registered reddit account to fetch contents from API
 - Registered account in [developer amazon services](https://developer.amazon.com/)
 - Above mentioned packages with python3 (Script not compatible with python2)
 - Ngrok for tunneling or deploying the flask app in server
(**Note**: Amazon accepts only `https` endpoints for developing alexa skills)


Run the Script and either tunnel the local flask app using ngrok or host it in a server and get the endpoint.
Create a new [alexa skill](https://developer.amazon.com/docs/custom-skills/steps-to-build-a-custom-skill.html).
Provide the endpoint while creating alexa skill. The Endpoint will receive POST requests when a user interacts with your Alexa Skill.


[Watch the Video](https://drive.google.com/file/d/163g5EmmB6x_u1cdFeTFWN6sAnnv7x3wJ/view?usp=sharing)
