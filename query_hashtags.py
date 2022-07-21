from config import host, database, myuser, mypass
import mysql.connector
import pandas as pd

data = {
	"Hashtag": [],
	"Engagements": [],
}
dataframe = pd.DataFrame(data)
myconn = mysql.connector.connect(host=host, database=database, user=myuser, password=mypass)
cursor = myconn.cursor(buffered=True)
sql_hashtags = "SELECT hashtag From engagements_hashtag Group By hashtag Order By hashtag Asc"
cursor.execute(sql_hashtags)
all_hashtags = cursor.fetchall()
for hashtag in all_hashtags:
	hashtag_check = (hashtag)
	sql_hashtag_count = "SELECT hashtag From engagements_hashtag Where hashtag = %s"
	cursor.execute(sql_hashtag_count,hashtag_check)
	hashtag_total = str(cursor.rowcount)
	dataframe.loc[len(dataframe.index)] = [hashtag[0], int(hashtag_total)]
print(dataframe.nlargest(100, 'Engagements'))