# Helsinki city bike data API

An API to provide city bike data in Helsinki Captal area, Finland. 

## End points
Journeys made during May - July 2021
`GET /api/journey`

Bike staitions
`GET /api/station`

## How to use

To clone and run this application you'll need Git and python installed on your computer. From your command line (on Mac): 

```
# Clone the repository by 
$ git clone https://github.com/shimpukka/helsinki-city-bike-app.git

# Go into the repository
$ cd helsinki-city-bike-app

# Create a virtual environment and activate it
$ python3 -m venv venv
$ source venv/bin/activate

# Install django and dependencies
$ pip install django 
$ pip install djangorestframework
$ python -m pip install django-cors-headers

# Run the app
$ python manage.py runserver

In your browser, open [http://localhost:8000/api/journey](http://localhost:8000/api/journey) to view journeys and [http://localhost:8000/api/station](http://localhost:8000/api/station) to view stations.

```

