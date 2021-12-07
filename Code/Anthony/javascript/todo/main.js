

const todoBtn = document.querySelector('#todo-btn')
const todoInput = document.querySelector('#todo-input')
const todoList = document.querySelector('#todo-list')


todoBtn.addEventListener('click', addTodo)
todoInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter'){
        addTodo()
    }
})

function addTodo(){
    // Get the value from input field
    const todoText = todoInput.value

    // Create a new <li>
    const li = document.createElement('li')
    // li.textContent = todoText

    // Create a <span> to store our todo text for styling purposes
    const span = document.createElement('span')

    // Add text to <span>
    span.textContent = todoText

    // Append <span> to <li>
    li.append(span)

    // Append <li> to <ul>
    todoList.append(li)

    // Reset input field to empty string
    todoInput.value = ''

    // ----------- Delete Button ------------------
    // Create <button> for deleting <li>'s
    const delBtn = document.createElement('button')
    delBtn.textContent = 'X'

    // Add <button> to <li>
    li.append(delBtn)

    // Add click event to <button> for deleting <li> from <ul>
    delBtn.addEventListener('click', function () {
        todoList.removeChild(delBtn.parentElement)
    })

    // ----------- Complete Button ------------------
    // Create <button> for completing <li>'s
    const completeBtn = document.createElement('button')
    completeBtn.textContent = '✅'

    // Add <button> to <li>
    li.append(completeBtn)

    // Add click event to <button> for completing todos
    completeBtn.addEventListener('click', function () {
        // Target the parent of <button>
        const parent = completeBtn.parentElement
        const span = parent.querySelector('span')

        // If the button is already completed, remove the line through and set color to black
        if (span.style.textDecoration === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'black'
            todoList.removeChild(parent)
            // .insertBefore() allows us to insert an HTML element before another
            todoList.insertBefore(parent, todoList.firstChild)
            completeBtn.textContent = '✅'
        // If button is not completed, line-through the span and set color to gray
        } else {
            span.style.textDecoration = 'line-through'
            span.style.color = 'gray'
            todoList.removeChild(parent)
            todoList.append(parent)
            completeBtn.textContent = '⎌'
        }
    })
}