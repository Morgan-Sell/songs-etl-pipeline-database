# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay (songplay_id int PRIMARY KEY, start_time TIME NOT NULL, user_id INT, level VARCHAR, song_id INT, artist_id INT,
                            session_id INT, location VARCHAR, user_agent VARCHAR)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user (user_id INT PRIMARY_KEY, title VARCHAR, artist_id INT, gender VARCHAR, level VARCHAR)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song (song_id INT PRIMARY_KEY, title VARCHAR, artist_id INT, year INT, duration TIME)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist (artist_id INT PRIMARY KEY, name VARCHAR, location VARCHAR, latitude DECIMAL, longitude DECIMAL)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time TIME NOT NULL, hour INT, day INT, week INT, month INT, year INT, weekday INT)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                            VALUES (%s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO user (user_id, title, artist_id, gender, level) VALUES (%s, %s, %s, %s, %s);""")

song_table_insert = ("""INSERT INTO song (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);""")

artist_table_insert = ("""INSERT INTO artist (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s);""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]