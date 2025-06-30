# Flask Person API

A simple Flask API for managing a list of people.

## Features

- List all people
- Search by name
- Find by UUID
- Add a new person
- Delete by UUID
- Custom error handling

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository:

git clone https://github.com/viejopeter/flask-person-api.git cd your-repo

2. Create a virtual environment and activate it:

python3 -m venv .venv

3. Go inside virtual environment:

source .venv/bin/activate

4. Install dependencies:

pip install Flask

5. Run the server:

flask --app server --debug run

## API Endpoints

- `GET /` — Hello World
- `GET /data` — Get data count
- `GET /name_search?q=<name>` — Search by first name
- `GET /count` — Get number of people
- `GET /person/<uuid>` — Find person by UUID
- `POST /person` — Add a new person (JSON body)
- `DELETE /person/<uuid>` — Delete person by UUID