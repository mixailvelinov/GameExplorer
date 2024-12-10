Deployed project -> https://gameexplorer-production-5b9c.up.railway.app/

instructions for running the project manually:

- download the project
- create an .env file and fill it in according to the provided template
- if you are not using the DB URL in the google docs provided in the survey, set up your DB with the variables below it in the .env temaplte
- setup your venv
- run pip install -r requirements.txt
- run python manage.py migrate
- run python manage.py setup_admin_roles (to create the Review Moderator group)
- run python manage.py runserver

This is a web app that allows users to rate and review games. The admins add games and have full CRUD permissions. The Review Moderators have limited CRUD and can delete reviews if they are offensive.
The admin can either use the web app to add games, platform and genres, and moderate reviews (there are views avaialble only for superusers) or they can do it via the Admin/API.
The Review Moderators can delete reviews from the Admin or directly through the app by tapping on the Delete button below each review.
