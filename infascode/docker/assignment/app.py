import time
from flask import Flask, request, jsonify
from peewee import Model, CharField, MySQLDatabase

app = Flask(__name__)

db = MySQLDatabase(
    "todo_db", user="root", password="root", host="persistance", port=3306
)


class Todo(Model):
    """
    A model representing todo item.
    """

    task = CharField()

    class Meta:
        database = db


def initialize_db():
    """
    Initialize the database connection and create tables.
    """
    max_retries = 10
    for i in range(max_retries):
        try:
            db.connect()
            print("Databasen ansluten.")
            db.create_tables([Todo])
            print("Tabeller skapade.")
            break
        except Exception as e:
            print(f"Databasfel: {e}")
            time.sleep(5)
    else:
        print("Kunde inte ansluta till databasen efter flera försök.")
        exit(1)


initialize_db()


@app.route("/todo", methods=["POST"])
def add_todo():
    """
    Add a new todo item to the database.
    """
    if not request.is_json:
        return jsonify({"error": "Data måste vara i JSON-format"}), 400
    data = request.get_json()
    task = data.get("task")
    if not task:
        return jsonify({"error": 'Fältet "task" saknas'}), 400
    try:
        todo = Todo.create(task=task)
        return jsonify({"message": "TODO tillagd", "id": todo.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/todo", methods=["GET"])
def get_todos():
    """
    Retrieve all todo items from the database.
    """
    try:
        todos = Todo.select()
        return jsonify([{"id": todo.id, "task": todo.task} for todo in todos]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# curl -X POST -H "Content-Type: application/json" -d '{"task": "Dricka vin"}' http://localhost:5000/todo
# curl -X GET http://localhost:5000/todo


# docker exec -it persistance mysql -u root -proot
# USE todo_db;
# DELETE FROM todo;
# SELECT * FROM todo;
# EXIT;
