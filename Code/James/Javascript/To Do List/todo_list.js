// used code and tutorial from: https://www.makeuseof.com/how-to-build-todo-list-app-using-javascript/

// Add an item to the list

/* Old

// Test

const submitButton = document.getElementById('submit');

submitButton.addEventListener('click', ()=>{
    alert('The form has been submitted');
})

// Athnony's Button:

const changeColorBtn = document.querySelector('#change-color-button')

changeColorBtn.addEventListener('click', function () {
    const changeColorInput = document.querySelector('#change-color-input')
    let color = changeColorInput.value
    const root = document.querySelector(':root')
    root.style.setProperty('--bg-color', color)
}) 
*/


// Connect buttons from HTML to Javascript 

const text = document.getElementById("text");
const addTaskButton = document.getElementById("add-task-btn");
const saveTaskButton = document.getElementById("save-todo-btn");
const checkTaskButton = document.getElementById("check-todo-btn");
const listBox = document.getElementById("listBox");
const saveInd = document.getElementById("saveIndex");

// Create array to store items

let todoArray = [];

// The Add Button

addTaskButton.addEventListener("click", (e) => {
    e.preventDefault();
    let todo = localStorage.getItem("todo");
    if (todo === null) {
      todoArray = [];
    } else {
      todoArray = JSON.parse(todo);
    }
    todoArray.push(text.value);
    text.value = "";
    localStorage.setItem("todo", JSON.stringify(todoArray));
    displayTodo();
});

// Display the list

function displayTodo() {
    let todo = localStorage.getItem("todo");
    if (todo === null) {
      todoArray = [];
    } else {
      todoArray = JSON.parse(todo);
    }
    let htmlCode = "";
    todoArray.forEach((list, ind) => {
      htmlCode += `<div>
      <p>${list}</p>
      <button onclick='check(${ind})' >Check</button>
      <button onclick='edit(${ind})' >Edit</button>
      <button onclick='deleteTodo(${ind})' >Delete</button>
   </div>`;
    });
    listBox.innerHTML = htmlCode;
}

// The Save Button

saveTaskButton.addEventListener("click", () => {
    let todo = localStorage.getItem("todo");
    todoArray = JSON.parse(todo);
    let id = saveInd.value;
    todoArray[id] = text.value;
    addTaskButton.style.display = "block";
    saveTaskButton.style.display = "none";
    checkTaskButton.style.display = "block"; // double check
    text.value = "";
    localStorage.setItem("todo", JSON.stringify(todoArray));
    displayTodo();
});
   
// Remove an item from the list (place into a 2nd list)

function deleteTodo(ind) {
    let todo = localStorage.getItem("todo");
    todoArray = JSON.parse(todo);
    todoArray.splice(ind, 1);
    localStorage.setItem("todo", JSON.stringify(todoArray));
    displayTodo();
}

// Mark an item as completed (check/strikethrough)

function check(ind)  {
    let todo = localStorage.getItem("todo");
    todoArray = JSON.parse(todo);
    let subject = todoArray[ind];
    let subject2 = subject.strike()
    todoArray.push(subject2);
    todoArray.splice(ind, 1);
    localStorage.setItem("todo", JSON.stringify(todoArray));
    displayTodo();
}


// Edit item

function edit(ind) {
    saveInd.value = ind;
    let todo = localStorage.getItem("todo");
    todoArray = JSON.parse(todo);
    text.value = todoArray[ind];
    addTaskButton.style.display = "none";
    saveTaskButton.style.display = "block";
    checkTaskButton.style.display = "none"; // double check
}
