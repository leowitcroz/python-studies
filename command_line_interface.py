
import modules.functions as functions
import time

prompt = 'Type add or show or edit, complete or exit: '

print( 'Now it is: ' + time.strftime('%b %d, %Y %H:%M:%S'))

while True:
	user_action = input(prompt)
	print('-' * 40 )
	user_action = user_action.strip()
	match user_action:

		case 'add' : 
			functions.addTodo()

		case 'show':
			functions.showAllTodos()
			
		case 'edit':
			functions.editTodo()

		case 'complete':
			todos = functions.showAllTodos()
			number = int(input('choose whitch todo is completed: '))
			number = number -1
			todos[number] = f'{todos[number].rstrip()} (DONE)' + '\n'
			functions.writeTodo(todos)

		case 'delete':
			todos = functions.showAllTodos()
			number = int(input('choose whitch todo to delete: '))
			number = number -1
			del todos[number]
			functions.writeTodo(todos)
			
		case 'exit':
			print("bye")
			break
		case whatever:
			print('Hey, you printed a unknown command')


	
		




 