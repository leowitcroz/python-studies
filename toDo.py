prompt = 'Type add or show or edit, complete or exit: '
todos = []

while True:
	user_action = input(prompt)
	user_action = user_action.strip()
	match user_action:
		case 'add' :
			todo = input("Enter a toDo: ")
			todos.append(todo.title())
			print('-' * 40 )
		case 'show':
			number = 0
			for item in todos:
				number += 1
				print(f'- {number}: {item}')
				number = number
				print('-' * 40 )
		case 'edit':
			number = int(input('Number of the to Do to edit: '))
			number  = number - 1
			newTodo = input(f'Former to Do is {todos[number]}, write the edition for this to Do: ')
			todos[number] = newTodo
			print('-' * 40 )
		case 'complete':
			number = 0
			for item in todos:
				number += 1
				print(f'- {number}: {item}')
				number = number
			number = int(input('choose whitch todo is completed: '))
			number = number -1
			todos[number] = f'{todos[number]} (DONE)'
		case 'exit':
			print("bye")
			break
		case whatever:
			print('Hey, you printed a unknown command')


	
		




 