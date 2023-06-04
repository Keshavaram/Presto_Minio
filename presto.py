import prestodb

conn = prestodb.dbapi.connect(
	host='192.168.49.2',
	port=32316,
	catalog="hive",
	schema="default",
	user="keshavaram"
)

cursor = conn.cursor()
query = "create table weather(dt varchar,place varchar,aqi varchar,co varchar,no varchar,no2 varchar,o3 varchar,so2 varchar,pm2_5 varchar,pm10 varchar,nh3 varchar) with (format = 'CSV', external_location = 's3a://test/')"
res = cursor.execute(query)
for i in res:
	print(i)
