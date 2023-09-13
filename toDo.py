prompt = 'Type add or show or edit or exit: '
todos = []

while True:
	user_action = input(prompt)
	user_action = user_action.strip()
	match user_action:
		case 'add' :
			todo = input("Enter a toDo: ")
			todos.append(todo.title())
		case 'show':
			for item in todos:
				print(item)
		case 'edit':
			number = int(input('Number of the to Do to edit: '))
			number  = number - 1
			newTodo = input(f'Former to Do is {todos[number]}, write the edition for this to Do: ')
			todos[number] = newTodo
		case 'exit':
			print("bye")
			break
		case whatever:
			print('Hey, you printed a unknown command')


	
		




 