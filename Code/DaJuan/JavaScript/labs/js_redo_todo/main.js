const todoInput = document.querySelector('#todo-imput')


todoBtn.addEventListener('click', addTodo)




// Delete Button
const delBtn = document.createElement('button')
delBtn.textContent = '❌'
li.append(delBtn)
delBtn.addEventListener('click', function() {
    todoList.removeChild(delBtn.parentElement)
})

// Complete Button
const completeBtn = document.createElement('button')
completeBtn.textContent = '✔'
li.append(completeBtn)
completeBtn.addEventListener('click', function() {
    const parent = completeBtn.parentElement
    const span = parent.querySelector
})