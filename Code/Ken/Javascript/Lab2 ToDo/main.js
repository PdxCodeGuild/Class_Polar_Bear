
const textField = document.querySelector('#user-input')
const btnNew = document.querySelector('#btn-new-task')
const btnRemove = document.querySelector('#btn-remove-task')
const list = document.querySelector('#task-list')
const completed = document.querySelector('#completed-list')


btnNew.addEventListener('click', function() {
    let task = document.createElement('li');
    task.innerHTML = textField.value;
    list.appendChild(task);
});


btnRemove.addEventListener('click', function() {
    list.removeChild(list.children[0])
});


list.addEventListener('click', function(event) {
    completed.appendChild(event.target);
    completed.style.textDecoration = 'line-through';
});


const body = document.querySelector('body')
body.style.fontFamily = 'sans-serif';


const buttons = document.querySelector('.btn')
buttons.style.backgroundColor = 'blue'
buttons.style.border = '1px dark-blue'
buttons.style.color = 'white'