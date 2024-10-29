from flask import Flask, request, jsonify
from peewee import Model, CharField, MySQLDatabase

app = Flask(__name__)

# Database connection configuration
db = MySQLDatabase(
    "todo_db", user="api_user", password="api_password", host="localhost", port=3306
)


class Todo(Model):
    task = CharField()

    class Meta:
        database = db


# Initialize the database and create the table if it doesn't exist
def initialize_database():
    if db.is_closed():
        db.connect()
    db.create_tables([Todo], safe=True)
    db.close()


# Connect to the database before each request
@app.before_request
def _db_connect():
    if db.is_closed():
        db.connect()


# Close the database connection after each request
@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()


@app.route("/todo", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task")
    todo = Todo.create(task=task)
    return jsonify({"id": todo.id, "message": "TODO tillagd"})


@app.route("/todo", methods=["GET"])
def get_todos():
    todos = [{"id": todo.id, "task": todo.task} for todo in Todo.select()]
    return jsonify(todos)


if __name__ == "__main__":
    # Initialize database when the app starts
    initialize_database()
    app.run(host="0.0.0.0", port=5000)


# curl -X POST -H "Content-Type: application/json" -d '{"task": "Dricka vin"}' http://100.118.35.85:5000/todo
# curl -X GET http://100.118.35.85:5000/todo
