# Sparkify Music Streaming App
## Analyzing User's Listening Habits



# Objective
Sparkify, a **fake** streaming music app that was **not** created in Sweeden, required help to be able to analyze their users' habits. 
The company had two raw data sources comprised of JSON metadata. One source was a log of user activity and the other was consisted of songs available on the app.

# Schema 
To examine users’ behaviors, Sparkify required a Star-schematized database which simplified queries and allows for fast aggregation. The database is in Third Normal Form (3NF) which removes duplicate data values and allows the Sparkify  to update the database by only revising one cell in one table.


![sparkifydb schema](./images/sparkify_schema.png)



# ETL Pipeline
1)	Execute `create_tables.py` to create the `sparkifydb` database and tables shown in the schema displayed above.
2)	Run `etl.py` which will execute the following actions:
    - Apply pandas to  process the JSON files, i.e. (listening) log and song dataset. 
    - Use pscycog2 to connect to the sparkifydb database.
    - Use the code from sql_queries.py to insert the raw data into its corresponding table. 
3)	In test.ipynb, perform desired analysis using PostgreSQL.

![etl pipeline](./images/etl_pipeline.png)

### Notes:
-  Must run `create_tables.py` before running `test.ipynb`, `etl.ipynb`, and `etl.py. 
-  The songs are filtered on "NextSong", a variable within the "action" attribute of the log data.


# Packages
- Pandas
- Psycopog2

