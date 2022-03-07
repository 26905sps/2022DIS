import sqlite3

#connect to database
con = sqlite3.connect('rockyconcrete.db')

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use the column headings
cur = con.cursor() #is the pointer to use in the database

# sql = """
#         select *
#         from customers
#         where town = 'Brisbane';"""
#
# cur.execute(sql)
# results = cur.fetchall()
# print(type(results))
# print(results)

#Parameter Query
town = input('Enter the town to search for: ')
min_cr = int(input('Enter the minimum credit limit: '))

sql = """
        select *
        from customers
        where town like ?
        and cr_limit >= ?;"""

cur.execute(sql,('%'+town+'%', min_cr))
results = cur.fetchall()

if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'lives in', row['street'], 'in', row['town'], 'and has credit limit of', row['cr_limit'])
else:
    print('No records found')
