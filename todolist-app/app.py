from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Путь к файлу где хранятся задачи
TODO_FILE = '/data/todos.json'

def load_todos():
    # Если файл не существует - возвращаем пустой список
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    # Сохраняем список задач в файл
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

@app.route('/todos', methods=['GET'])
def get_todos():
    # Возвращаем все задачи
    return jsonify(load_todos())

@app.route('/todos', methods=['POST'])
def add_todo():
    # Добавляем новую задачу
    todo = request.json
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    return jsonify({"status": "ok"})

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    # Удаляем задачу по индексу
    todos = load_todos()
    if index >= len(todos):
        return jsonify({"error": "not found"}), 404
    todos.pop(index)
    save_todos(todos)
    return jsonify({"status": "deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
