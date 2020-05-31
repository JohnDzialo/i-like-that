# i-like-that

## Description

Hey!  Do you like reading people's posts?  Do you like rating posts in the hopes of emotionally abusing the OP?

Then this is the app for you.  Post a message, read other's messages, then Up vote or Down vote the posts as you see fit.


## Setup

Build the docker-compose script and bring up the containers.

```bash
docker-compose build
docker-compose up
```

Nginx will be listening on http://localhost:8080 and will route traffic to the flask backend.

## Usage

Create a new post

```bash
curl --request POST \
  --url http://localhost:8080/posts/ \
  --header 'content-type: application/json' \
  --data '{
   "body": "when the posting begins the roasting begins"
}'
```

Select all posts as json

```bash
curl --request GET \
  --url http://localhost:8080/posts/
```

Select a post by id, get id by running get all posts

```bash
curl --request GET \
  --url http://localhost:8080/posts/<id>
```

Delete a post by id, get id by running get all posts

```bash
curl --request DELETE \
  --url http://localhost:8080/posts/<id>
```

Increment likes for a post, get id by running get all posts

```bash
curl --request PUT \
  --url http://localhost:8080/posts/<id>/likeit/up/
```

Decrement likes for a post, get id by running get all posts

```bash
curl --request PUT \
  --url http://localhost:8080/posts/<id>/likeit/down/
```

## Run Tests

```bash
python -m pytest
```

## DB Migrations

Use the manage.py scripts to handle any db migrations

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## TODO

Better schema validation for incoming requests.
100% test coverage
