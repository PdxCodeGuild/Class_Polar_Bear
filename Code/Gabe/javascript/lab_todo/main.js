const todoBtn = document.querySelector('#todo-button');
const todoInput = document.querySelector('#todo-input');

todoBtn.addEventListener('click', function () {
  const todo = todoInput.value;

  let todosList = document.querySelector('#todos-list');

  let todoItem = document.createElement('li');
  todoItem.innerHTML=`<span>${todo}</span>`;

  let completedBtn = document.createElement('button');
  completedBtn.textContent = 'Complete?';
  completedBtn.addEventListener("click",(e) => completeButton(e));

  let deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete?';
  deleteBtn.addEventListener("click",(e) => deleteButton(e));

  todosList.appendChild(todoItem);
  todoItem.appendChild(completedBtn);
  todoItem.appendChild(deleteBtn);

  setTimeout(() => {
    todoInput.value = '';
  }, 1);
})

todoInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    const todo = todoInput.value;

    let todosList = document.querySelector('#todos-list');


    let todoItem = document.createElement('li');
    todoItem.innerHTML=`<span>${todo}</span>`;

    let completedBtn = document.createElement('button');
    completedBtn.textContent = 'Complete?';
    completedBtn.addEventListener("click",(e) => completeButton(e));

    let deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete?';
    deleteBtn.addEventListener("click",(e) => deleteButton(e));

    todosList.appendChild(todoItem);
    todoItem.appendChild(completedBtn);
    todoItem.appendChild(deleteBtn);

    setTimeout(() => {
      todoInput.value = '';
    }, 1);
  }
})

function deleteButton(e) {
  e.path['1'].remove();
}

function completeButton(e) {
  if (e.path['1'].parentNode.id === 'todos-list' && !null) {
    let completedList = document.querySelector('#completed-list');
    let completedTodo = document.createElement('li');
    completedTodo.innerHTML = `<span>${e.path['1'].querySelector('span').textContent}</span>`;

    let deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete?';
    deleteBtn.addEventListener("click",(e) => deleteButton(e));

    completedList.appendChild(completedTodo);
    completedList.appendChild(deleteBtn);
    setTimeout(() => {
      e.path['1'].remove();
    }, 1);
  }
  // if (e.path['1'].parentNode.id === 'completed-list' && !null) {
  //   let todosList = document.querySelector('#todos-list');

  //   let todoItem = document.createElement('li');
  //   todoItem.innerHTML=`<span>${e.path['1'].querySelector('span').textContent}</span>`;

  //   let completedBtn = document.createElement('button');
  //   completedBtn.textContent = 'Complete?';
  //   completedBtn.addEventListener("click",(e) => completeButton(e));

  //   let deleteBtn = document.createElement('button');
  //   deleteBtn.textContent = 'Delete?';
  //   deleteBtn.addEventListener("click",(e) => deleteButton(e));

  //   todosList.appendChild(todoItem);
  //   todosList.appendChild(completedBtn);
  //   todoItem.appendChild(deleteBtn);
  //   setTimeout(() => {
  //     e.path['1'].remove();
  //   }, 1);
  // }
}