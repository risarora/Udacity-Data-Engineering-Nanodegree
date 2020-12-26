# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop     = "DROP table if exists users"
song_table_drop     = "DROP table if exists songs"
artist_table_drop   = "DROP table if exists artists"
time_table_drop     = "DROP table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table songplays(
    songplay_id  serial PRIMARY KEY,
    start_time timestamp,
    user_id VARCHAR,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id VARCHAR,
    location VARCHAR,
    user_agent VARCHAR
);

""")

user_table_create = ("""
create table users (
    user_id  serial PRIMARY KEY,
    first_name VARCHAR ( 30 ) NOT NULL, 
    last_name VARCHAR ( 30 ) NOT NULL, 
    gender VARCHAR(2), 
    level int
);

""")

song_table_create = ("""
create table songs (
song_id  serial PRIMARY KEY,
title varchar, 
artist_id varchar,
year varchar,
duration time
);

""")

artist_table_create = ("""
create table artists (
artist_id  serial PRIMARY KEY,
name VARCHAR ( 30 ) NOT NULL, 
location varchar, 
latitude decimal, 
longitude decimal
);

""")

time_table_create = ("""create table time (
start_time timestamp, 
hour int, 
day int, 
week int, 
month int , 
year int , 
weekday boolean)

""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays(songplay_id ,start_time ,user_id ,level ,song_id ,artist_id ,session_id ,location ,user_agent ) 
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    on conflict (songplays) DO NOTHING;
""")

user_table_insert = ("""
    insert into users (user_i, first_name, last_name, gender, level ) 
    values(%s,%s,%s,%s,%s)
    on conflict (users) DO NOTHING;

""")

song_table_insert = ("""
    insert into songs (song_id, title, artist_id, year ,duration time)
    values (%s,%s,%s,%s,%s)
    on conflict (songs) DO NOTHING;

""")

artist_table_insert = ("""
    insert into artists (artist_id, name, location, latitude, longitude)
    values(%s,%s,%s,%s,%s)
    on conflict (artists) DO NOTHING;
""")


time_table_insert = ("""
    insert into time(start_time ,hour ,day ,week ,month ,year ,weekday )
    values(%s, %s, %s, %s, %s, %s, %s)
    on conflict (time) DO NOTHING;

""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]