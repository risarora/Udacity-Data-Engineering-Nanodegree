# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop     = "DROP table if exists users"
song_table_drop     = "DROP table if exists songs"
artist_table_drop   = "DROP table if exists artists"
time_table_drop     = "DROP table if exists time"

# CREATE TABLES
create_table_test = ("""
create table test(
    test_id  int,
    test_name varchar
    );
""")

songplay_table_create = ("""
create table songplays(
    songplay_id serial PRIMARY KEY,
    start_time TIMESTAMP ,
    user_id int NOT NULL ,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id int,
    location VARCHAR,
    user_agent VARCHAR
);
""")

user_table_create = ("""
create table users (
    user_id serial PRIMARY KEY,
    first_name VARCHAR, 
    last_name VARCHAR , 
    gender VARCHAR(2), 
    level varchar(10)
);

""")

song_table_create = ("""
    create table songs (
    song_id  serial PRIMARY KEY,
    title varchar, 
    artist_id varchar,
    year varchar,
    duration decimal
);
""")

artist_table_create = ("""
    create table artists (
    artist_id  varchar PRIMARY KEY,
    artist_name VARCHAR NOT NULL, 
    artist_location varchar, 
    artist_latitude decimal, 
    artist_longitude decimal
);
""")

time_table_create = ("""create table time (
    start_time timestamp PRIMARY KEY, 
    hour int, 
    day int, 
    week int, 
    month int , 
    year int , 
    weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays( start_time ,user_id ,level ,song_id ,artist_id ,session_id ,location ,user_agent ) 
    values(%s,%s,%s,%s,%s,%s,%s,%s)
    on conflict DO NOTHING;
""")

user_table_insert = ("""
    insert into users (user_id, first_name, last_name, gender, level ) 
    values(%s,%s,%s,%s,%s)
    on conflict (user_id) DO UPDATE 
    SET level = EXCLUDED.level;

""")

song_table_insert = ("""
    insert into songs ( title, artist_id, year ,duration )
    values (%s,%s,%s,%s)
    on conflict DO NOTHING;
""")

artist_table_insert = ("""
    insert into artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    values(%s,%s,%s,%s,%s)
    on conflict DO NOTHING;
""")


time_table_insert = ("""
    insert into time(start_time ,hour ,day ,week ,month ,year ,weekday )
    values(%s, %s, %s, %s, %s, %s, %s)
    on conflict DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, artists.artist_id
    FROM songs INNER JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.artist_name = %s
    AND songs.duration = %s   
""")

# QUERY LISTS

create_table_queries = [time_table_create, user_table_create, create_table_test,songplay_table_create, song_table_create, artist_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]