Launch the server with

`docker-compose up`

Then visit the site at http://localhost:8080

Launch the seeder with:

`docker exec -ti infact_server_web_1 python manage.py seed --mode=refresh`