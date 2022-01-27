const renderTodos = todos => {
    let trashTodos = document.querySelectorAll('.todo');
    for(let trashTodo of trashTodos) {
        trashTodo.remove();
    }
    let htmlTodos = todos.map(todo => {
        let appendTodo = document.createElement('li');

        if(todo.completed) {
            appendTodo.className = 'list-group-item todo todo-completed';
            appendTodo.innerHTML = todo.text;
        } else {
            appendTodo.className = 'list-group-item todo d-flex justify-content-between align-items-center';
            appendTodo.innerHTML = `${todo.text}
                <div>
                    <button class="btn btn-sm btn-primary todo-complete">That's completed / C'est fini</button>
                    <button class="btn btn-sm btn-danger todo-delete ml-2">Remove / Effacer</button>
                </div>`;
            appendTodo.querySelector('.todo-delete').onclick = () => {
                todoStorage.removeTodo(todo.id);
            }
            appendTodo.querySelector('.todo-complete').onclick = () => {
                todoStorage.completeTodo(todo.id);
            }
        }

        return appendTodo;
    });

    for(let item of htmlTodos) {
        document.querySelector('.list-group').append(item);
    }
}

const storage = function() {
    let todos = [];
    let todosCount = 1;
    return {
        addTodo: newTodo => {
            todos.push({
                id: ++todosCount,
                text: newTodo,
                completed: false
            });
            renderTodos(todos);
        },
        removeTodo: todoId => {
            todos = todos.filter(todoItem => todoItem.id !== todoId);
            renderTodos(todos);
        },
        completeTodo: todoId => {
            const newTodos = todos.filter(todoItem => todoItem.id !== todoId);
            const completedTodo = todos.filter(todoItem => todoItem.id === todoId)[0];
            completedTodo.completed = true;
            todos = [...newTodos, completedTodo];
            renderTodos(todos);
        }
    }
}
const todoStorage = storage();

document.getElementById('addTodo').onclick = e => {
    let newTodoValue = document.getElementById('addTodo-input').value;
    newTodoValue = newTodoValue.trim();
    if(!newTodoValue.length) {
        document.querySelector('.err-empty').classList.remove('hidden');
        setTimeout(() => {
            document.querySelector('.err-empty').classList.add('hidden');
        }, 3000)
    } else {
        todoStorage.addTodo(newTodoValue);
        document.getElementById('addTodo-input').value = '';
    }
}