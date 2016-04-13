import sqlite3 as lite
import yaml

try:
    with open("../../resources/settings.yml", "r") as s_file:
        settings = yaml.load(s_file)
except yaml.YAMLError:
    logger.error("Cannot parse settings file.")
    sys.exit(-1)
except IOError:
    logger.error("Cannot open settings file.")
    sys.exit(-1)

conn = lite.connect("../resources/" + settings["DB_FILE"])

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
              damaged       text,
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
