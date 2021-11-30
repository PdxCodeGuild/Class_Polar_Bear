const todoBtn = document.querySelector('#todo-button');
const todoInput = document.querySelector('#todo-input');
const todos = [];
const completedTodos = [];

todoBtn.addEventListener('click', function () {
  const todo = todoInput.value;
  todos.push(todo);

  let todosList = document.querySelector('#todos-list');


  let todoItem = document.createElement('li');
  let completedBtn = document.createElement('button');
  let deleteBtn = document.createElement('button');

  todoItem.textContent = todo;
  completedBtn.textContent = 'Complete?';
  completedBtn.setAttribute("id", "completed-button");
  deleteBtn.textContent = 'Delete?';
  deleteBtn.setAttribute("id", "delete-button");

  todosList.appendChild(todoItem);
  todoItem.appendChild(completedBtn);
  todoItem.appendChild(deleteBtn);

})

const deleteBtn = document.querySelector('#delete-button');

deleteBtn.addEventListener('click', function () {
  console.log('hello')
})