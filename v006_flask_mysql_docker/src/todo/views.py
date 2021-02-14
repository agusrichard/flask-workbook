from . import todo

@todo.route('/')
def index():
    return 'Todo!'