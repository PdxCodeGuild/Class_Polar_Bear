// emojis
const myEmojies = ['✅', '❌']

// add event lister to catch input field 'enter'
let inputField = document.querySelector('#todo-input');
inputField.addEventListener('keypress', function (event) {
    if (event.key === 'Enter'){
        addToMyList()
    }
})

// add event listener to catch button being clicked
let todoButton = document.querySelector('#todo-button');
todoButton.addEventListener('click', addToMyList);

// counter
let counter = 1;

// create main function
function addToMyList () {   
    // pull the user input data from the input field and store it in a variable
    let userInputValue = inputField.value;

    // access the list and assign the users input to it
    let myList = document.querySelector('#todo-u-list');

    // create a new List Item when user enters new input
    if (userInputValue) {
        // add list items to our html file and assign the users input value to it
        let li = document.createElement("li");
        li.textContent = userInputValue;
        myList.appendChild(li);
        li.setAttribute('id', 'todo-list-item' + counter);

        // add first button with green check
        let newGreenButton = document.createElement("button");
        newGreenButton.textContent = myEmojies[0];
        myList.appendChild(newGreenButton);
        newGreenButton.setAttribute('id', 'todo-new-green-button' + counter);


        // add second button with red check
        let newRedButton = document.createElement("button");
        newRedButton.textContent = myEmojies[1];
        myList.appendChild(newRedButton);
        newRedButton.setAttribute('id', 'todo-new-red-button' + counter);

       // access li
       let myLi = document.getElementById('todo-list-item' + counter);

        // Add event listener and function to line-through item
        let greenButton = document.querySelector('#todo-new-green-button' + counter);
        greenButton.addEventListener('click', function () {
            // undo line-through conditional statement
            if (myLi.style.textDecoration === 'line-through') {
                myLi.style.textDecoration = 'none';
            } else {
                myLi.style.textDecoration = 'line-through';
            }
        })

        // Add event listener and function to remove item
        let redButton = document.querySelector('#todo-new-red-button' + counter);
        redButton.addEventListener('click', function () {
            myLi.remove();
            redButton.remove();
            greenButton.remove();
        })

    }
    
    // add to our counter
    counter += 1;

    // set input field value to empty
    inputField.value = "";  
}
