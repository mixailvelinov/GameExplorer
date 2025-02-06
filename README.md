# GameExplorer

**The application is live at [GameExplorer Production](https://gameexplorer-production-5b9c.up.railway.app/)**


GameExplorer is a web app that allows users to rate and review games. The platform supports role-based access, enabling Admins and Review Moderators to perform specific actions. 

## Test Users
You can use the following credentials to test different user types:
- admin: email **admin@admin.com** pass **admin**
- review moderator: email **mod@mod.com** pass **moderator12**

You can also create a new user and assign them as Review Moderator and is_staff through the admin (after logging in as an admin first).

## Features
### Game Reviews and Ratings:
- Users can rate and review games by selecting the game and clicking on the **Mark as Played** button.
- Reviews are visible on the game pages. All reviews for a specific user can be checked by clicking on their profile and then **Reviews**.
- Users can send **suggestions** to admins if they don't see a specific games in the library.
- A welcome email is sent to the user when registering.
- Can access public views only.
### Admin Features:
- **Full CRUD** (Create, Read, Update, Delete) permissions for managing games, platforms, genres, and reviews.
- Review moderation via the web app or **Admin/API** interface.
- In the web app, they have a nav bar with more options. They can add **games**, **platforms** and **genres**.
- The game suggestions list can be viewed by clicking on **Add games** and then selecting **Check user suggestions** located below the form. When a suggestion is fulfilled, it can be deleted by clicking on the **bin icon** next to the suggestion.
- They can delete reviews by tapping on the **Delete** button below the review in quesiton.
### Review Moderators:
- **Limited CRUD permissions** - they can delete ofensive reviews, while the admins focus more on the game content.
- Delete reviews directly through the admin, API or directly through the web app - a **Delete** button will show below every review.
- Editing reviews is avaialble only for the user who has written it. 


## Setup Instructions
Follow these steps is you wish to run the project locally:

### 1. Download the Project
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
