import mysql.connector
from mysql.connector import errorcode

config = {
  "user": "ktaylor",
  "password": "kendall",
  "host": "127.0.0.1",
  "database": "movies",
  "raise_on_warnings": True
}

try:
  db = mysql.connector.connect(**config)
  print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
  input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The supplied username or password are invalid")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The specified database does not exist")
  else:
    print(err)

cursor = db.cursor()
cursor.execute("SELECT * From STUDIO")
studio = cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
for studio in studio:
  print("studio_id: {}\n studio_name: {}\n".format(studio[0], studio[1]))

cursor = db.cursor()
cursor.execute("SELECT * From GENRE")
genre = cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for genre in genre:
  print("genre_id: {}\n genre_name: {}\n".format(genre[0], genre[1]))

cursor = db.cursor()
cursor.execute("SELECT * From FILM WHERE film_runtime < 120")
film = cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for film in film:
  print("film_name: {}\n film_runtime: {}\n".format (film[1], film[3]))

cursor = db.cursor()
cursor.execute("SELECT * From film ORDER BY film_director")
film = cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for film in film:
  print("film name: {}\n film_director: {}\n".format(film[1], film[4]))




