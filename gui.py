import modules.functions as functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a to-do')
input_box = PySimpleGUI.InputText(tooltip='Enter todo', key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.getTodo() , key='todos', enable_events=True, size=[45,10])
edit_button = PySimpleGUI.Button('Edit')
delete_button = PySimpleGUI.Button('Delete')
complete_button = PySimpleGUI.Button('Complete')

window = PySimpleGUI.Window('My To-Do App', 
                            layout=[[label], [input_box],[list_box ,[add_button,edit_button,complete_button, delete_button]]], 
                            font=('Helvitica', 12))


while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.getTodo()
            new_todo = values['todo'] + '\n'
            if str(new_todo).rstrip() == '':
                continue
            else:
                todos.append(str(new_todo).title())
                functions.writeTodo(todos)
                
                window['todo'].update(value='')
                window['todos'].update(values=todos) #used to refresh the list
           
        case 'Edit':
            
            todos = functions.getTodo()
            if values['todos'] != []:
                   edit_todo = values['todos'][0]
                   new_todo = values['todo']
                   index = todos.index(edit_todo)
                   todos[index] = str(new_todo).title().rstrip() + '\n'
                   
                   if todos[index].rstrip() == '':
                        continue
                   else:
                        functions.writeTodo(todos)
        
                   window['todo'].update(value='')
                   window['todos'].update(values=todos) #used to refresh the list
            else:
                edit_todo = ''

        case 'Complete':
             complete_todo = values['todos'][0]
             
             todos = functions.getTodo()
             index = todos.index(complete_todo)
             todos[index] = todos[index].rstrip() + ' (DONE) \n'
             print(todos[index])
             functions.writeTodo(todos)
             window['todo'].update(value=''.rstrip())
             window['todos'].update(values=todos)
             
        case 'Delete':
            delete_todo = values['todos'][0]
            todos = functions.getTodo()
            index = todos.index(delete_todo)
            del todos[index]
            functions.writeTodo(todos)
            window['todo'].update(value='')
            window['todos'].update(values=todos)
            
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        
        case PySimpleGUI.WIN_CLOSED:
            break
        
window.close()  