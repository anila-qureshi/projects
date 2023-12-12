# project
## About Me:
This project is aimed to bring end-to-end pipeline management of data. I have a data scientist background and have been working as a data analyst within revenue, sales and operations for the past 2.5 years. I have had my hand at KPI creation. 
<br>
# Project Background: 
This project aims at scraping data from the web. I have chosen Github. Within Github I have picked 3 repositories to scrape. I want to retrieve the hash so that I know I am not retrieving duplicates. I am also retrieving the commit messages, the timestamp, the number of insertions, the number of deletions, and the author. From here, I would like to look at the data and create KPIs to track the productivity of its contributors. Are there more insertions or deletions during a certain part of the day or a certain day of the week? Are there specific words associated with such insertions or deletions? What can this say about contributors? <br>
<br>
I will start by doing some Natural Language Processing. This will help me to create buckets for the most common words used in messages and allow me to see whether there is a correlation between commit messages with # Insertions and # Deletions. I will then look to see any patterns from here. 
<br>
I will finish this project by creating a dashboard using Tensorflow's Pytorch.
# Table of Contents: 
- api_scraper: it is a python script that retrieves data on github repositories. this script will then export the data as a clean csv file.
- load_to_postgres.py: is a python script that will take this clean csv and load it into your local Postgres. (This can help analysts do some analysis using an IDE, I personally use DBeaver because it is free and simple)
- commit_data: is the clean exported csv from the python scrape
- testing_api_scraper.ipynb: this is a jupyter notebook that shows how I personally tested whether my scripts work or not. You can feel free to use the code to see if yours works
- testing_etl_connection.ipynb: testing the connection between the api and my local computer to retrieve data. again this is to test whether my python script works <br>
- exploratory_data_analysis.ipynb: a general EDA of the data
- analysis_via_commit_messages.ipynb: This jupyter notebook will explore KPI creations and behaviors by what is written within the commit messages.
<br>
<br>

