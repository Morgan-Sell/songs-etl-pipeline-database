# Sparkify Music Streaming App
### Database and ETL Pipeline to Enable Product and User Analytics

<img src="https://github.com/Morgan-Sell/songs-etl-pipeline-database/blob/main/images/music_fest.jpg" width="800" weight="200">

# Objective
Sparkify, a **fake** streaming music app that was launched during the COVID-19 pandemic, required help to enables its data analysts to evaluate trends and user habits. 
There were two raw data sources comprised of JSON metadata. One source was a log of user activity and the other consisted of songs available on the app.

# Schema 
To quickly assess user behaviors, Sparkify required a Star-schematized database, called `sparkifydb`, which simplified queries and allowed for fast aggregation. The database achieved Third Normal Form (3NF) which removed duplicate data values and allowed startup to update the database by only revising one cell in one table.

![sparkifydb schema](./images/sparkify_schema.png)

# ETL Pipeline
1)	Execute `create_tables.py` to construct the `sparkifydb` database and tables shown in the schema displayed above.
2)	Run `etl.py` to perform the following actions:
    -  Process the JSON files, i.e. (listening) log and song datasets;
    - Connect to the `sparkifydb` database;
    -  Run `sql_queries.py` to insert the raw data into its corresponding table. 
3) Perform desired analysis using PostgreSQL In `test.ipynb`.

![etl pipeline](./images/etl_pipeline.png)

### Notes:
-  Must run `create_tables.py` before running `test.ipynb`, `etl.ipynb`, and `etl.py`.
-  The songs are filtered on "NextSong", a variable within the "action" attribute of the log data.

# Example Queries

Now that Sparkify has a schematized database, the startup can perform product/market and user analysis. The following are two examples:

#### Top 10 Markets 
![top 10 markets](./images/top10_markets.png)

#### Top 5 Most Frequent Users
![top 5 Markets](./images/top5_users.png)

# Packages
- Pandas
- Psycopog2

