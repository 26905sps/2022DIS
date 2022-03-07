import sqlite3

#connect to database
con = sqlite3.connect('rockyconcrete.db')

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use the column headings
cur = con.cursor() #is the pointer to use in the database

name = input('Enter name: ')

sql = """
        select max(order_date) as order_date, max(order_no) as order_no, cust_no, curr_bal, cust_name
        from customers c, orders o
        where c.cust_no = o.cust_no
        and cust_name like ?;"""

cur.execute(sql,('%'+name+'%',))
results = cur.fetchall()

if len(results) > 0:
    for row in results:
        print(row['cust_name'], 'Customer Number:', row['cust_no'], 'Current Balance:', row['curr_bal'], 'Order Number:', row['order_no'],'Order Date:', row['order_date'])
else:
    print('No records found')
