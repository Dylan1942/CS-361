from flask import Flask, render_template, request, redirect, url_for, jsonify
from momentum_tasks import db, Task 

app = Flask(__name__)

# Set the URI for the database you want to use
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Initialize the db with the Flask app
db.init_app(app)

@app.route("/tasks")
def list_tasks():
    # Query all tasks from the database
    tasks = Task.query.all()
    # Render the tasks.html template, passing in tasks as a context variable
    return render_template("momentum_tasks.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    if request.method == "POST":
        # Create a new instance of the Task
        new_task = Task(
            name=request.form['name'],
            description=request.form.get('description', ''),  
            status=request.form.get('status', 'Not Started'),
            priority=request.form.get('priority', 0),
            due_date=request.form.get('due_date', '')
        )

        # Add the new task to the database
        db.session.add(new_task)
        db.session.commit()

        # Redirect to the tasks list
        return redirect(url_for('list_tasks'))

    # If the method is not POST, just redirect to the tasks list
    return redirect(url_for('list_tasks'))

@app.route('/remove_task', methods=['POST'])
def remove_task():
    task_id = request.form.get('task_id')
    if task_id:
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        else:            
            pass
    return redirect(url_for('list_tasks', message='Task successfully deleted.'))

# Runs the app
if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()
    # Start the Flask development server
    app.run(debug=True)
