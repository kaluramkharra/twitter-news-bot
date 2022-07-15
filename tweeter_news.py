import requests
import datetime
import tweepy


#-------------NewsApi credentials--------------------
api="put your api key from news api"
#----------------------------------------------------



#-----------Twitter credentials------------------------
#you can find all this credentials on twitter developer account
twitter_auth_keys = {
        "consumer_key"        : "your customer key",
        "consumer_secret"     : "customer secret key",
        "access_token"        : "access token",
        "access_token_secret" : "access token secret"
        }
#----------------------------------------------------
auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
api = tweepy.API(auth)


#----------------------------------------------------
def news():
    categories=["general","business","sports","technology","entertainment","health","science"]
    for cat in categories:
    	catnews=requests.get("https://newsapi.org/v2/top-headlines?country=in&category="+cat+"&apiKey="+api_key).json()['articles']
    	for article in catnews:
    		#print(type(article))
    		img=article["urlToImage"]
    		title=article['title']
    		#print(title)
    		desc=article['description']
    		content=article['content']
    		url=article['url']
    		tweet=str(""+title+"   #"+cat+"    article: "+url)
    		if type(str) == str:
    			status=api.update_status_with_media(img, tweet)
    		else:
    			status = api.update_status(status=tweet)
news()   	   	
#----------------------------------------------------   	   			

#---------------------STOCK MARKET-----------------
def stock():
	stock=requests.get("https://newsapi.org/v2/everything?q=nse&apiKey="+api_key).json()['articles']
	i=0
	for article in stock:
		 	if i<11:
		 		img=article['urlToImage']
		 		title=article['title']
		 		desc=article['description']
		 		content=article['content']
		 		url=article['url']
		 		print(url)
		 		tweet=str(title+"   #stockmarket   article: "+url)
		 		if type(str) == str:
		 			status=api.update_status_with_media(img, tweet)
		 		else:
		 			status = api.update_status(status=tweet)
		 		i+=1
		 		
stock()
#----------------------------------------------------


#--------------------CORONA------------------------
def corona():
	corona=requests.get("https://newsapi.org/v2/everything?q=corona&apiKey="+api_key).json()['articles']
	i=0
	for article in corona:
		 	if i<11:
		 		img=article['urlToImage']
		 		title=article['title']
		 		desc=article['description']
		 		content=article['content']
		 		url=article['url']
		 		print(url)
		 		tweet=str(title+"   #corona  article: "+url)
		 		if type(str) == str:
		 			status=api.update_status_with_media(img, tweet)
		 		else:
		 			status = api.update_status(status=tweet)
		 		i+=1
		 	
corona()
#---------------------------------------------------