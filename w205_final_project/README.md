# Project 3: Data Driven Bets
# Alexandra Drossos, Courtney Smith, Blake Bormes, Austin Sanders

# Description of Problem

Sports betting is a growing market, and it is becoming legal in more and more states. A lot of betting predictions are based on what others have already bet, including people who follow their "gut instinct" or bet on their favorite teams regardless of statistical predictions. We want to create a service in the growing market of sports betting to help make weekly predictions for sports bettors and give live updates on games our customers have bet on. For example, the weekly predictions would give information such as, "The Titans are favored to beat the Texans at a -1200 Money Line (12 to 1 odds) with a -14 point spread. Earlier in the year, they lost to the Jets while they were favored at a -900 Money Line with a -11 point spread. Therefore, the Titans can get beaten by teams when significantly favored to win. If the Titans start the game poorly, you may want to consider betting on the underdog." The live updates on games customers bet on could be similar to this example: If you bet Packers -3, the app will update you that "2nd quarter Packers are down 6 points, so they need to score 10 points to cover the spread." Additionally, we could further explore the idea of tracking a customer's weekly betting performance in a future version of the application.

- [Data Source](https://sportsdata.io/developers/api-documentation/nfl#/fantasy/nfl-v3-projections-projected-player-game-stats-by-week-w-injuries-lineups-dfs-salaries)

# Research Questions
Given this business context, we have determined the following initial questions we would like to analyze given our data set: 
- If I'm considering betting on the 49'ers, could the app tell me the spread, over under, and money line?
- If I'm reviewing all teams' performance compared to what the spread predictions were, can the app let me know a list of the final scores, spread predictions, and delta ordered from biggest difference to smallest?
- Given a bettor's team and spread, can the app let me know what the game score is and how far above or below the score the spread is?
- Can the app analyze the biggest upsets based on money line for all teams for a given week?


# Tools Utilized

Google Cloud Platorm (GCP) - Establish Virtual Machine (VM) and infrastructure for
data pipeline.

Kafka - The queue for the files. Publish and consume messages for the dataset.

Zookeeper - The main node managing kafka.

Spark - Transforms the dataset to store it in a readable and queryable format.

Hadoop Distributed File System (HDFS) - Storage system for the readable tables.

Jupyter Notebook - Runs spark functions and queries; used for exploratory analysis. 

# Pipeline Description
To ingest this data from the SportsDataIO API and make it available to our consumers to query, we had to construct a complete streaming data pipeline. The docker-compose.yml inherently provides a good overview of the tools we used to accomplish this. However, it will be more intuitive to go in sequential order by use to describe the pipeline functionality. For starters, this entire pipeline is executed through the command line, and therefore the explanation will be accompanied with the various commands that were used. At the front end of the pipeline is the SportsDataIO API. Surprisingly, this was the only free NFL data API we could find that functioned properly with mostly reliable data. For future work, we would recommend using a subscription API like GoalServe or SportsRadar. However, for the purposes of this implementation project, this free API was sufficient.

The first task we had to run was to spin up our pipeline from our docker-compose.yml file. This was accomplished by running the following command:

```
docker-compose up -d
```

The next step was to create our kafka topics, “games” for streaming live game updates and "season" for a batch pull of all data for the season so far. 
A Kafka topic is basically a category you declare to organize data. This data is sent to and received from the topic in the form of messages (or packets of data). In this example, we will be calling the SportsDataIO API to receive NFL games scores data and that will be sent into the ‘games’ kafka topic. This will be our streaming data. Additionally, we will be creating the topic 'season' for a batch data call that pulls scores from the whole season. The command below, in setting up the kafka topic, essentially creates the conduits for the scores and season data to be pushed to and received from:

```
docker-compose exec kafka kafka-topics --create --topic games --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181
```

```
docker-compose exec kafka kafka-topics --create --topic season --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:32181
```

For this project, we used Zookeeper with Kafka. Zookeeper’s job is to manage the cluster. It coordinates brokers and is a consistent file system for all configuration information. 

Next, we run our Flask Application from our “mids” virtual machine using the following command:

```
docker-compose exec mids env FLASK_APP=/w205/W205_Project_3/nfl_api.py flask run --host 0.0.0.0
```

At a high level, Flask is a web framework written in Python, providing developers with tools and libraries to build web applications. It creates a server from which you can send and receive requests. In this command, we’re running our Flask server, with the application defined in the nfl_api.py file. The --host argument is set to 0.0.0.0 to enable the server to be publicly available, meaning it’s open to non-local connections as well. Now that we have our Flask application running, we can go into nfl_api.py to unpack what will actually happen when this application is run. 

The Flask application, held within the `nfl_api.py` file, calls the SportsDataIO API, pulls in the data from the call, and logs it to the kafka topics via a Kafka producer that is initialized in the line:

producer = KafkaProducer(bootstrap_servers='kafka:29092')

Firstly, the get_game_data function calls the API. SportsDataIO offers many API endpoints for NFL data. The endpoint that this function utilizes is the ScoresByDate endpoint, which pulls the scores for each game by date. If you pass in the current date and there are games being played, the scores are live updated every 5 minutes. The other endpoint we utilized in a separate function was the ScoresByWeek endpoint, which is used for our consumers to get historical game data. Both of these endpoints were accessed via an HTTP GET request with our unique API key. After calling the API, the response is stored in .json() format and passed to the log_to_kafka function. Because this response “event” was stored as one big JSON string, rather than representing the x number of games going on, we used a for loop to parse each game out and have it sent to the Kafka producer as a separate event. Meaning, if there are 10 games going on when the API is called, the log_to_kafka function will send 10 separate events to the Kafka producer. 

Now with our “mids” server running our Flask application, we execute the following Apache Bench command to execute the call to our API and send the data to our Kafka producer:
 
```
for i in {1..6}; do
  docker-compose exec mids \
    ab -n 1 -H "Host: user2.att.com" \
      http://localhost:5000/get_game_data
  sleep 600
done
```

This command calls the API through the /get_game_data route once every 10 minutes for an hour. This is because we’re wanting our consumers to have access to live score updates. The API we’re using only updates its data every 5 minutes, so these intervals will be hopefully spaced out enough to provide meaningful updates. That was one limitation with our API. Additionally, because we are using a free version of the API, SportsDataIO disclosed that about 10% of the data would be scrambled. 

While the apache bench command is running, we can set up a Kafka consumer watcher. This will consume all the messages in the Kafka topic:

```
docker-compose exec mids kafkacat -C -b kafka:29092 -t games -o beginning
```

Next, we use Spark to extract the streaming events from our Kafka topic and write them to HDFS using the following command:

```
docker-compose exec spark spark-submit /w205/W205_Project_3/extract_games_stream.py
```

The `extract_games_stream.py` file defines the schema for our data and uses Spark Streaming to initiate a Spark session, extract the data from our Kafka topic, convert it to our schema, and write the events to a parquet file every 6 minutes (located at path /tmp/games). These parquet files will essentially be partitions of the entire dataframe we will eventually create in analysis.

Now that we have our streaming pipeline set up, we run parallel commands for the batch data call. The below command executes one call to the API using the /get_season_data route. This function retreives the complete season scores and pushes it to the 'season' kafka topic:

```
docker-compose exec mids curl http://localhost:5000/get_season_data
```

We'll also, as we did with the streaming data, set up a Kafka consumer watcher for the batch data API call, so that we can see what is being consumed by the 'season' topic:

```
docker-compose exec mids kafkacat -C -b kafka:29092 -t season -o beginning
```
Now that the batch data has been consumed by the Kafka 'season' topic, we will run the extract_games.py file, which is a Spark job. This file creates a Spark session, reads in the data from the 'season' topic, converts it from an RDD to a DataFrame with our defined schema, and sends that dataframe to a parquet file in HDFS (located at path tmp/seasoon). 
```
docker-compose exec spark spark-submit /w205/W205_Project_3/extract_games.py
```

After this Spark job has been submitted with the command below, and both our streaming and batch pipelines are complete, we can check the tmp/season and tmp/games folders in HDFS to make sure that the parquet files landed there from our Spark jobs. 
```
docker-compose exec cloudera hadoop fs -ls /tmp/season
docker-compose exec cloudera hadoop fs -ls /tmp/games
```

After confirming that the parquet files exist in the expected folders, we will want to open pyspark environment in a jupyter notebook to conduct our analysis. 
```
docker-compose exec spark env PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port 8889 --ip 0.0.0.0 --allow-root --notebook-dir=/w205/' pyspark
```

Ideally, the next steps for us would have been to save an external table in Hive and then query that table from Presto. However, the Presto connection was consistently being very finnicky for us. It would load in perfectly at times, but then other times return nothing from our Hive table. After working with the TAs for an extended period of time, we did not feel confident in using Presto as a tool for our querying and analysis. We could not gaurantee that our daata consumers would not run into trouble using this tool. As an alternative, we did all the querying and analysis in pyspark.

For the streaming data, we read in the parquet files in tmp/games, and then used a spark SQL to create an external table and save it as a separate parquet file located at tmp/games_out. This outputted parquet file is a table with all 10 of the partition parquet files combined. Once we read back in the tmp/games_out parquet file and turn it into a dataframe, we will have all 10 API calls represented in 1 table. Please see Analysis.ipynb for the remainder of the analysis.


# Links to Files

- [Project_3 Analysis Notebook](https://github.com/mids-w205-de-sola/project-3-austinsanders22/blob/assignment/Analysis.ipynb)
- [NFL API File](https://github.com/mids-w205-de-sola/project-3-austinsanders22/blob/assignment/nfl_api.py)
- [Spark Streaming File](https://github.com/mids-w205-de-sola/project-3-austinsanders22/blob/assignment/extract_games_stream.py)
- [Spark Batch File](https://github.com/mids-w205-de-sola/project-3-austinsanders22/blob/assignment/extract_games.py)
- [Docker-Compose File](https://github.com/mids-w205-de-sola/project-3-austinsanders22/blob/assignment/docker-compose.yml)

### Descriptions of Files

- API_test.ipynb: initial test to pull data from the API and to understand the data structure and data present
- docker-compose.yml: docker-compose file to set up the required images including zookeeper, kafka, cloudera, spark, presto, and mids
- extract_games_stream.py: Our .py file to extract events from kafka and stream them into HDFS
- extract_games.py: Our .py file to extract events from kafka and land them in HDFS (batch)
- history2.txt: Terminal history of commands used to execute pipeline, with explanation 
- nfl_api.py: File to pull data from the API including the get_game_data event
- scores.json: JSON file with an example output of the data from our API
- spark_testing.ipynb: Read json data with Spark from Parquet for test analysis of our data
- Project_3.ipynb: analysis to answer business questions
