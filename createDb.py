import sqlite3 as lite

conn = lite.connect('database.db')

print("Connected to database.")
c = conn.cursor()

c.execute('''CREATE TABLE users
             (id    integer primary key,
              name  text not null,
              email text not null)''')

c.execute('''CREATE TABLE requests
             (id            integer primary key,
              user_id       integer not null,
              search_text   text not null,
              auction_type  text,
              price_min     text,
              price_max     text,
              used          text,
              foreign key(user_id) REFERENCES users(id))''')

c.execute('''CREATE TABLE categories
             (request_id        integer not null,
              category          text not null,
              foreign key(request_id) references requests(id))''')

c.execute('''CREATE TABLE products
             (request_id        integer not null,
              product_id        text not null,
              foreign key(request_id) references requests(id))''')

conn.commit()
conn.close()
print("Database succesfully created.")
