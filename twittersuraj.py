import tweepy
import time
import string
import operator
import sys

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)

	# The top n users who have tweeted the most for the entire timeline.


def totalUsers():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twit=myFile.readlines()
    g = {}
    for dat in twit:
       
        fileTemp = dat.split()
        if fileTemp[0] in g:
            g[fileTemp[0]] +=1
        else:
            g[fileTemp[0]] = 1
    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)
 
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    outputFile.write("The top 10 users who have tweeted the most for the entire timeline: \n")
    for i in range (0,10):
        outputFile.write("User Name " + g[i][0] + "\n\n")
        
    outputFile.close
totalUsers()

# The top n users who have the maximum followers.
def maxFollowers():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twit=myFile.readlines()

    g = {}
    for dat in twit:
        fileTemp = dat.split()
        if fileTemp[0] not in g:
            g[fileTemp[0]] = int(fileTemp[-2])

    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    outputFile.write("The top 10 users who have the maximum followers: " + "\n\n")

    for i in range (0, 10):
        outputFile.write("Username: " + g[i][0] + "\n\n")
    outputFile.close
maxFollowers()

# The top n tweets which have the maximum retweet count.
def retweetCount():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        twit=myFile.readlines()

    g = {}
    for dat in twit:
  
        fileTemp = dat.split()
        y = len(fileTemp)-2
        tweet = "\""
        for x in range (4, y):
            tweet += fileTemp[x] + " "
        tweet += " ::::;:::: " + fileTemp[0]
  
        if tweet not in g:
            g[tweet] = int(fileTemp[-1])

    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)
    outputFile.write("The top 10 tweets that have the max retweet count: " + "\n\n")

    for x in range (0, 10):
        outputFile.write("\n Tweet: " +
                      g[x][0].split("::::;::::")[0]  + "\n\n")
    outputFile.close
retweetCount()

# The top n users who have tweeted the most for every hour.
def usersPerHour():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as myFile:
        data=myFile.readlines()

    g = {}
    for dat in data:
        fileTemp = dat.split()
        fileTemp2 = fileTemp[1].split(":")
        twitTemp = fileTemp[0] + " " + fileTemp2[1]
        if twitTemp in g:
            g[twitTemp]+=1
        else:
            g[twitTemp]=1
    g = sorted(g.items(), key = operator.itemgetter(1), reverse = True)

    g2={}
    totalUsersIn = 0
    for dat in g:
        totalUsersIn+=1
        if(dat[0].split()[1]) in g2:
            g2[dat[0].split()[1]]+=1
        else:
            g2[dat[0].split()[1]]=1
    g2 = sorted(g2.items(), key = operator.itemgetter(1))

    totalEntriesToPrint = 10*len(g2)
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
   
    outputFile.write("The top 10 users who have tweeted the most for every hour: " + "\n\n")
    for x in range (0,len(g2)):
   
        mSearch = 10
        
       
        for dat in g:
            if mSearch == 0:
                break
            if dat[0].split()[1] == g2[x][0]:
                outputFile.write("Username: " + dat[0].split()[0] + "\n\n")
                
                mSearch-=1
    outputFile.close
usersPerHour()



    
