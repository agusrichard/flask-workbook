import json
from flask import jsonify, request

from . import todo
from .. import db
from .model import Todo


@todo.route('/', methods=['POST'])
def create():
    try:
        print('this is the create route')
        title = request.json.get('title')
        description = request.json.get('description')

        new_todo = Todo(title=title, description=description)
        db.session.add(new_todo)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Success to create todo',
            'data': {
                'id': new_todo.id,
                'title': new_todo.title,
                'description': new_todo.description
            }
        })
    except:
        return jsonify({
            'success': False,
            'message': 'Failed to create todo',
            'data': dict()
        })

@todo.route('/', methods=['GET'])
def get_all():
    try:
        todos = Todo.query.all()
        print('todos', todos)
        return jsonify({
            'success': True,
            'message': 'Success to get all todos',
            'data': [{
                'id': val.id,
                'title': val.title,
                'description': val.description
            } for val in todos]
        })
    except:
        return jsonify({
            'success': False,
            'message': 'Failed to get all todos',
            'data': dict()
        })

@todo.route('/<int:todo_id>', methods=['GET'])
def get_one(todo_id):
    try:
        todo_result = Todo.query.filter_by(id=todo_id).first()
        return jsonify({
            'success': True,
            'message': f'Success to get single todo with id {todo_id}',
            'data': {
                'id': todo_result.id,
                'title': todo_result.title,
                'description': todo_result.description
            }
        })
    except:
        return jsonify({
            'success': False,
            'message': f'Failed to get single todo with id {todo_id}',
            'data': dict()
        })

@todo.route('/<int:todo_id>', methods=['PUT'])
def update(todo_id):
    try:
        todo_result = Todo.query.filter_by(id=todo_id).first()
        todo_result.title = request.json.get('title')
        todo_result.description = request.json.get('description')
        db.session.commit()

        return jsonify({
            'success': True,
            'message': f'Success to update single todo with id {todo_result.id}',
            'data': {
                'id': todo_result.id,
                'title': todo_result.title,
                'description': todo_result.description
            }
        })
    except:
        return jsonify({
            'success': False,
            'message': f'Failed to update single todo with id {todo_id}',
            'data': dict()
        })

@todo.route('/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    try:
        todo_result = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(todo_result)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': f'Success to delete single todo with id {todo_result.id}',
            'data': {
                'id': todo_result.id,
                'title': todo_result.title,
                'description': todo_result.description
            }
        })
    except:
        return jsonify({
            'success': False,
            'message': f'Failed to update single todo with id {todo_id}',
            'data': dict()
        })