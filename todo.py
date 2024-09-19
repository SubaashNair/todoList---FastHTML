from fasthtml.common import *

# Create a FastHTML app
app, rt = fast_app()

# Create an in-memory database for todos
todos = []

@rt('/')
def get():
    # Create a form for adding new todos
    add_form = Form(
        Input(id='new-todo', name='title', placeholder='Enter a new todo'),
        Button('Add', type='submit'),
        hx_post='/add-todo',
        hx_target='#todo-list',
        hx_swap='beforeend'
    )
    
    # Create a list to display todos
    todo_list = Ul(id='todo-list')
    for i, todo in enumerate(todos):
        todo_list.append(Li(
            todo,
            Button('Delete', 
                   hx_delete=f'/delete-todo/{i}',
                   hx_target='closest li',
                   hx_swap='outerHTML'
            )
        ))
    
    # Combine all elements
    content = Container(
        H1("My Todo List"),
        add_form,
        todo_list
    )
    
    return Titled("Todo List", content)

@rt('/add-todo')
def post(title: str):
    todos.append(title)
    return Li(
        title,
        Button('Delete', 
               hx_delete=f'/delete-todo/{len(todos)-1}',
               hx_target='closest li',
               hx_swap='outerHTML'
        )
    )

@rt('/delete-todo/{index}')
def delete(index: int):
    if 0 <= index < len(todos):
        del todos[index]
    return ''  # Return an empty string to remove the item from the list

# Run the app
serve()