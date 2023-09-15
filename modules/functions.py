def showAllTodos():
    number = 0
    file = open('todos.txt', 'r')
    todos = file.readlines()
    for item in todos:
        number += 1
        print(f'- {number}: {item}')
        number = number
        print('-' * 40 )
    return todos

def writeTodo(todos):
    file = open('todos.txt', 'w') 
    file.writelines(todos)

def addTodo():
    todo = input("Enter a toDo: ") + '\n'
    file = open('todos.txt', 'r')
    todos = file.readlines()
    todos.append(todo.title())
    writeTodo(todos)

def editTodo():
    file = open('todos.txt', 'r')
    todos = file.readlines()
    
    print('Here are your current ToDos:' + '\n')

    showAllTodos()

    number = int(input('Number of the to Do to edit: '))
    number  = number - 1

    newTodo = input(f'Former to Do is {todos[number].rstrip()}, write the edition for this to Do: ') + '\n'
    todos[number] = newTodo.title()

    writeTodo(todos)
    print('-' * 40 )

def getTodo():
    file = open('todos.txt', 'r')
    todos = file.readlines()
    return todos
    
    
    