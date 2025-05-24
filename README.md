# Mtcars-Flask-Api
This Repository contains all files needed to create a simple statistical model, create an image using Docker and builds a server using Google Cloud Run using Flask API.

The Mtcars dataset is being used. 6 variables are used to predict the miles per gallon (mpg) of the inputted car. 

## Files

| File | Description |
|------|-------------|
| `mtcars.csv` | Mtcars dataset used for the model |
| `prediction.py` | Python script containing the prediction function, with the GradientBoost model |
| `server.py` | Python script containing the Flask application for the API |
| `Dockerfile` | Instructions for the Docker Image |
| `docker-compose.yml` | Script used when creating a Docker Image |
| `requirements.txt` | Python Dependencies|

## Predictor Variables

These are the variables used for the model

 - 'cyl'
 - 'disp'
 - 'hp'
 - 'drat'
 - 'wt'
 - 'qsec'


## How it works

### 1. Clone this repo

### 2. Build your Docker Image

Open terminal and change your directory to where you have downloaded this repo, and run the script:

```bash
docker compose up -d
```
To check whether the API is working, you can run this script:

```bash
curl http://localhost:5050/
```
Expected Output:
```bash
server is up - nice job!
```

### 3. Test the model Locally

You can test the model by running a sample command:
```bash
curl -H "Content-Type: application/json" -X POST -d '{"wt":3.73,"am":1,"qsec":17.6,"gear":4,"drat":3.07,"cyl":8}' "http://localhost:5050/predict_mpg"
```
Expected Output:
```json
{"predicted mpg": 18.4314781529401}
```

### 4. Push Docker Image to Docker hub to create Repository

Push the created docker image and create a repository in Docker hub, under your account username. 

### 5. Deploy to Google Cloud Run

Create a service using Google Cloud Run, and use the URL created and check whether the live API is working. 
The command below is a sample, that accesses the API created by me.
```bash
curl -X POST "https://mtcars-flask-app-883217264014.us-west2.run.app/predict_mpg" -H "Content-Type: application/json" -d '{"cyl":"8","disp":"200","hp":"180","drat":"3.10","wt":"3.15","qsec":"20.0"}'
```
Expected Output:
```json
{"predict mpg": 18.64315608891703}
```



