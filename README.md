# FastHTML Todo List Application

This is a simple Todo List application built using [FastHTML](https://fasthtml.dev), a Python framework for building reactive web apps. The app allows users to view, add, and delete todo items, all with smooth updates to the page using HTMX.

## Features

- **Add a Todo**: Add a new todo item by typing it into the input box and pressing the "Add" button.
- **Delete a Todo**: Each todo item has a "Delete" button, allowing you to remove it from the list without refreshing the entire page.
- **Real-time updates**: The application uses HTMX to dynamically update the page content without full page reloads.

## Installation

### Prerequisites

Before running this application, ensure you have Python installed on your system. You'll also need to install the following dependencies:

1. **FastHTML**: This is the core framework for the app.
   
   Install FastHTML using pip:
   ```bash
   pip install fasthtml
   ```

2. **HTMX**: FastHTML integrates seamlessly with HTMX to enable real-time updates.

   HTMX is included in the FastHTML package, so no additional installation is needed.

### Clone the Repository

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/SubaashNair/todoList---FastHTML.git
   ```

2. Navigate into the project directory:
   ```bash
   cd todoList---FastHTML
   ```

### Run the Application

1. Run the Python file to start the application:
   ```bash
   python todo_app.py
   ```

2. Open your browser and go to `http://localhost:5001` to access the app.

### Folder Structure

```
todoList---FastHTML/
│
├── todo_app.py        # Main application file
├── README.md          # Project documentation (this file)
└── requirements.txt   # List of dependencies (optional, can be generated)
```

## Usage

1. On the home page, you will see an input field where you can enter a new todo item.
2. Enter the todo and click the "Add" button. The item will immediately appear in the list.
3. To delete an item, click the "Delete" button next to the respective todo.

## Code Overview

- **Main Application (`todo_app.py`)**:
  - The app consists of three main routes:
    - `/`: Displays the todo list and allows users to add new todos.
    - `/add-todo`: Adds a new todo item to the list.
    - `/delete-todo/{index}`: Deletes a todo item based on its index.
  - HTMX is used to handle form submissions and updates to the todo list without requiring full page reloads.
  
### Example Code

Here’s a snippet of the core logic for adding and deleting todo items:

```python
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
```

## Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastHTML](https://fasthtml.dev) for the Python framework used to build this application.
- [HTMX](https://htmx.org) for providing real-time updates without requiring full page reloads.

