prompt = 'Type add or show or exit: '
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
		case 'exit':
			print("bye")
			break

	
		




 