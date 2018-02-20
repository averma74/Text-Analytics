# Text-Analytics
Comparing and Contrasting Expert Twitter Accounts on Cybersecurity Utilizing Thesaurus Methods for Text Analytics

The purpose of this project is provide text analytics on a large data set. The large data set consists of thousands of tweets.  The tweets that we will be analyzing are from 10 Cybersecurity related Twitter accounts. By collecting data, we will try to find the difference from each cybersecurity expert’s profile, and compare them. Analyzing this large mass of tweets, we hope to build a Thesaurus containing relevant Cybersecurity related concepts. The steps to create a Thesaurus on this data includes; tokenizing, removing stop words, stemming the data. Through this analysis, we will prove that preprocessing and other machine learning techniques can be used to provide meaningful analysis on a large amount of text data.

The list of Cybersecurity experts we chose are:
1.	@Cyber
2.	@CLTCBerkeley
3.	@NJCybersecurity
4.	@NISTcyber
5.	@NortonOnline
6.	@DarkReading
7.	@TheCyberSecHub
8.	@threatintel
9.	@symantec
10.	@McAfee

Elements:
1. tweet_dumper.py : It's the tweepy python program file. We just have to put the twitter id in the program and it gives a csv file of the id's tweeter data.
2. MainProgram.py : This is the program which performs the data processing. We provide the tweepy file as input to this program and it's output is the final thesaurus for the given profile.
3. ExpertTweets Folder: Contains the tweepy output files.
4. ThesaurusCSVs Folder: Contains the mainProgram.py's output files which are the tweeter user's fingerprint.
