# **UBER WEBSCRAPING AND TIME SERIES PREDICTION**

First, scrapes for fare data on Uber estimate website using *Selenium*
    - Then charts it and gather this data in a csv file
        - After cloning, do create a csv file to hold data scraped from website

Second, trained several(hope to be several) time series prediction models including LSTM and Facebook Prophet to identify key trends and is capable of predicting future fare estimates.

## TO USE WEBSCRAPER:

1) Clone project
2) Import from ```requirements.txt```
2) Add data.csv to ```webscraper``` directory
3) Run main_Webscraper once, and in that automated window, create a Chrome profile of the email that
   you are using to scrape data off of Uber.
	- Primary issue was that to get a proper fare estimate, Uber requires you to login, hence the 
	  Chrome profile.
4) From then on, it should run smoothly

