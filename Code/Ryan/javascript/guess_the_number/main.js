
let startGameButton = document.querySelector('#start-game-button')
let choiceButtons = document.querySelector('#choice-buttons')
let result = document.querySelector('#result')

function generateButtons () {
    // clearing out all previous tags inside html
    choiceButtons.innerHTML = ''
    result.textContent = ''    
    let difficultyLevel = document.querySelector('#difficulty-level')
    let maxGuess = parseInt(difficultyLevel.value)
    // create random number within the range
    let randomNumber = Math.floor(Math.random() * maxGuess) + 1
    // looping
    for (let i = 1; i <= maxGuess; i++){
        // console.log(maxGuess)
        // create a new element on html
        let newButton = document.createElement('button')    
        // add text to the button
        newButton.textContent = i
        newButton.addEventListener('click', function (event) {
            // look at target to see what button was clicked
            // text content
            // event.target.textContent to get the specific button being clicked on
            // console.log(event)
            // console.log(typeof event.target.textContent)
            let button = event.target    
            if (parseInt(event.target.textContent) === randomNumber){
                    //typically add this to css
                    button.style.backgroundColor = 'green'
                    console.log('Correct!!!')
                    result.textContent = 'Correct!'
            } else { 
                    button.style.backgroundColor = 'red'
                    result.textContent = 'Try again.'
            }
        })
        let choiceButtons = document.querySelector('#choice-buttons')
        // put the button on the page
        choiceButtons.append(newButton)
    }
}


startGameButton.addEventListener('click', generateButtons)