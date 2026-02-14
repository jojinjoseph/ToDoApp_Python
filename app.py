from flask import Flask, render_template, request, redirect, url_for
import functions as fn

app = Flask(__name__)

# Load initial todos
todolist = fn.read_todos()

@app.route("/", methods=["GET", "POST"])
def index():
    global todolist
    if request.method == "POST":
        # Add new todo
        if "todo" in request.form:
            todo = request.form["todo"].strip()
            if todo:
                todolist.append(todo + "\n")
                fn.add_values(todolist)
        # Remove completed todos
        elif "remove" in request.form:
            todo_to_remove = request.form["remove"]
            todolist = [todo for todo in todolist if todo.strip() != todo_to_remove]
            fn.add_values(todolist)
        return redirect(url_for('index'))

    return render_template("index.html", todolist=todolist)

if __name__ == "__main__":
    app.run(debug=True)
