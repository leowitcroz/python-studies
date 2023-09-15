import modules.functions as functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a to-do')
input_box = PySimpleGUI.InputText(tooltip='Enter todo', key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.getTodo() , key='todos', enable_events=True, size=[45,10])
edit_button = PySimpleGUI.Button('Edit')

window = PySimpleGUI.Window('My To-Do App', 
                            layout=[[label], [input_box , add_button],[list_box ,edit_button]], 
                            font=('Helvitica', 12))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.getTodo()
            new_todo = values['todo'] + '\n'
            todos.append(str(new_todo).title())
            functions.writeTodo(todos)
            
            window['todos'].update(values=todos) #used to refresh the list
           
        case 'Edit':
            edit_todo = values['todos'][0]
            new_todo = values['todo'] + '\n'
            
            todos = functions.getTodo()
            index = todos.index(edit_todo)
            todos[index] = str(new_todo).title()
            functions.writeTodo(todos)
            
            window['todos'].update(values=todos) #used to refresh the list
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        
        case PySimpleGUI.WIN_CLOSED:
            break
        
window.close()  