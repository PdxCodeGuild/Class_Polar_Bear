
const todoInput = document.querySelector('#todo-input')
const createTodoBtn = document.querySelector('#create-todo-btn')
let todoList = document.querySelector('#todo-list')
let completedTodoList = document.querySelector('#completed-todo-list')
let counter = 0

// Creates a Todo
createTodoBtn.addEventListener('click', function (){
    counter += 1
    let todoText = todoInput.value
    let todoValue = document.createElement('span')
    todoValue.setAttribute('id', counter)
    todoValue.textContent = `${todoText}`
    const todoCmplBtn = document.createElement('cmpl-button')
    todoCmplBtn.innerHTML = '&#10003;'


    // Swaps the list the Todo is on and adds/removes strikethrough -- not working at the moment
    todoCmplBtn.addEventListener('click', function (event){
        let grandparentID = todoCmplBtn.parentNode.parentNode.id
        if (grandparentID == 'todo-list'){
            var newGp = completedTodoList
            var image = '&#x21ba;'
        } else if (grandparentID == 'completed-todo-list'){
            var newGp = todoList
            var image = '&#10003;'
        }

        let chosenTodo = event.target.parentNode
        event.target.innerHTML = image
        event.target.parentNode
        newGp.append(chosenTodo)
    })
    
    // swaps line-through/ none styles for span
    const li = document.createElement('li')
    const span = document.createElement('span')
    todoCmplBtn.addEventListener('click', function (event){
        const parent = todoCmplBtn.parentElement
        const span = parent.querySelector('span')
        if (span.style.textDecoration === 'line-through'){
            span.style.textDecoration = 'none'
            span.style.color = 'black'
        } else {
            span.style.textDecoration = 'line-through'
            span.style.color = 'black'
        }
    })


    // Removes the Todo from either list
    let todoDeleBtn = document.createElement('dele-button')
    todoDeleBtn.textContent = 'X'
    todoDeleBtn.addEventListener('click', function (event){
        let grandparent = todoCmplBtn.parentNode.parentNode.id
        if (grandparent == 'todo-list'){
            var variList = todoList
        } else if (grandparent == 'completed-todo-list'){
            var variList = completedTodoList
        }
        variList.removeChild(event.target.parentNode)
    })

    if (todoText == ''){
        alert('Please, enter some input text.')
    } else{
        let todoLi = document.createElement('li')
        todoLi.setAttribute('id', counter)
        todoLi.append(todoCmplBtn,' ', todoDeleBtn, '⟶', todoValue)
        let appendTodo = todoList.appendChild(todoLi)
    }
})