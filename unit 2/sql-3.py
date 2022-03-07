import sqlite3

#connect to database
con = sqlite3.connect('rockyconcrete.db')

#create a cursor/pointer to navigate the database
con.row_factory = sqlite3.Row #enables us to use the column headings
cur = con.cursor() #is the pointer to use in the database

a = int(input('1. Get Customer Details, 2. Get Order Details, 3. Get Product Details, 4. Quit'))

if a == 1:
    b = input('Enter Customer Name')
    sql = """
            select * 
            from customers
            where cust_name like ?
            """
    cur.execute(sql, ('%'+b+'%',))
    results = cur.fetchall()

    if len(results) > 0:
        for row in results:
            print(row['cust_no'],row['cust_name'],row['street'],row['town'],row['post_code'],row['cr_limit'],row['curr_bal'])
    else:
        print('No records found')

if a == 2:
    b = input('Enter Order Number')
    sql = """
            select * 
            from order_details
            where order_no like ?
            """
    cur.execute(sql, ('%'+b+'%',))
    results = cur.fetchall()

    if len(results) > 0:
        for row in results:
            print(row['order_no'],row['prod_code'],row['order_qty'],row['order_price'])
    else:
        print('No records found')

if a == 3:
    b = input('Enter Product Name')
    sql = """
            select * 
            from products
            where prod_code like ?
            """
    cur.execute(sql, ('%'+b+'%',))
    results = cur.fetchall()

    if len(results) > 0:
        for row in results:
            print(row['prod_code'],row['description'],row['prod_group'],row['list_price'],row['qty_on_hand'],row['remake_level'],row['remake_qty'])
    else:
        print('No records found')

if a == 4:
    print('Goodbye')
    exit()