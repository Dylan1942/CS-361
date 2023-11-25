# CS-361
Software Engineering 
Installation
Prerequisites
Python 3.6 or higher
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-SocketIO
PostgreSQL Database

Clone the Repository
git clone https://github.com/your-repository/Momentum-App.git
Navigate to the Application Directory
cd Momentum-App
Install Dependencies
pip install -r requirements.txt
Set Environment Variables
Set FLASK_APP, and database URI in your environment.
export FLASK_APP=runner.py
export DATABASE_URL='your-database-uri'
Initialize the Database
flask db upgrade
Running the Application
Development Server
flask run

Authentication
Login Endpoint: Authenticate users and manage sessions.
Registration Endpoint: Allow new users to register.

Task Management
Create Task Endpoint: Add new tasks to the system.
List Tasks Endpoint: Retrieve a list of tasks, filterable by user and status.
Update Task Endpoint: Modify existing tasks.
Delete Task Endpoint: Remove tasks from the system.
