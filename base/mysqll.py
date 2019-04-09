import mysql.connector

##https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320107391860b39da6901ed41a296e574ed37104752000
conn = mysql.connector.connect(user='root', password='**1234##', database='koushao')
cursor = conn.cursor()
cursor.execute('select * from koushao.`T_activityComment` limit 10')
values = cursor.fetchall()
print(values)