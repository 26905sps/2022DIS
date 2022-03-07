import sqlite3

#connect to database
con = sqlite3.connect('people.db')

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use the column headings
cur = con.cursor() #is the pointer to use in the database
#Parameter Query
name = input('name: ')
age = int(input('age: '))
sex = input('Sex: ')
earns = int(input('Earns'))
likes = input('Like: ')
dislikes = input('Dislike: ')

sql = """
        insert
        into members (name, age, sex, earns, likes, dislikes)
        values (?,?,?,?,?,?); """

cur.execute(sql,(name,age,sex,earns,likes,dislikes,))
con.commit()
results = cur.fetchone()
for row in results:
    print(row['name'],row['age'],row['sex'],row['earns'],row['likes'],row['dislikes'])
