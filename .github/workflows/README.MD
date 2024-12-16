# What this application do?
- Send an API request for the following link: https://rickandmortyapi.com/api/character
- Cheack each page and filter only the characters that are meet the criterias Status "Alive" the   origin "Earth" and Species "Human" 
- the application returns for each character the following output: Rick Sanchez,Earth,https://rickandmortyapi.com/api/character/avatar/1.jpeg
- the application has the ability to export the results into a CSV file
- The application is runing on port 8000 and runing with RestAPI
## RestAPI endpoints
- /results - the results after filtering the characters from all the pages
- /csv - export the results into csv file
- /healthcheck - will return 2 values about the API(/results) and (CSV/csv) services if they are runing with status code.

## How to build the application?
- Please make sure that Docker engine is runing
- To build this application please run the following command
```
docker build -t pythonimage .
```
## How to run the application inside container?
- The application is running on port 8000 the continer port should be the same port number
- Please run the following command to run on docker container
```
docker run -dit --name pythonapp -p 8000:8000 pythonimage:latest
```

## How to access the endpoints?
- To access the enpoints open your browser and past this endpoints
```
localhost:8000/results
localhost:8000/csv
localhost:8000/healthcheck
```
