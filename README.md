# GameExplorer

**The application is live at [GameExplorer Production](https://gameexplorer-production-5b9c.up.railway.app/)**


GameExplorer is a web app that allows users to rate and review games. The platform supports role-based access, enabling Admins and Review Moderators to perform specific actions. Users can explore games, add reviews, and interact with the content added by admins.

## 1. Features
### Game Reviews and Ratings:
- Users can rate and review games.
- Reviews are visible on the game pages.
- Users can send suggestions to admins if they don't see a specific games in the library.
- A welcome email is sent to the user when registering.
- Can access public views only.
### Admin Features:
- Full CRUD (Create, Read, Update, Delete) permissions for managing games, platforms, genres, and reviews.
- Review moderation via the web app or Admin/API interface.
### Review Moderators:
- Limited CRUD permissions - they can delete ofensive reviews, while the admins focus more on the game content.
- Ability to delete reviews directly through the app, via the Admin panel or API.


## Setup Instructions
Follow these steps to run the project locally:

## 1. Download the Project
Clone or download the project files to your local machine.

### 2. Create the .env File
- Use the provided .env template in the project to create your .env file.
- Fill in the variables based on the template - if you are using the provided DB URL (referenced in the Google Docs that was submitted with the SoftUni servey), set it in the .env file.
- Otherwise, configure your database using the variables listed in the .env template.
### 3. Set Up the Virtual Environment
Run the following commands to set up your Python virtual environment:

```python -m venv venv```
``` venv\Scripts\activate ```

### 4. Install Dependencies
Install the required Python packages using the requirements.txt file:
```pip install -r requirements.txt```

### 5. Run Database Migrations
Apply the database migrations to set up the required tables. The migrations contain some pre-filled content for games:

```python manage.py migrate```

### 6. Set Up Admin Roles
Create the Review Moderator group with the appropriate permissions:


```python manage.py setup_admin_roles```

### 7. Start the Development Server
Run the application locally:

```python manage.py runserver```
