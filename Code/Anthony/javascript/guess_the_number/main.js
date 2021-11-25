
let startGameButton = document.querySelector('#start-game-button')
let choiceButtons = document.querySelector('#choice-buttons')
let result = document.querySelector('#result')
let randomNumber

function generateButtons() {
    choiceButtons.innerHTML = ''
    result.textContent = ''
    let difficultyLevel = document.querySelector('#difficulty-level')
    let maxGuess = parseInt(difficultyLevel.value)
    randomNumber = Math.floor(Math.random() * maxGuess) + 1
    console.log(randomNumber)
    
    for (let i = 1; i <= maxGuess; i++){
        let newButton = document.createElement('button')
        newButton.textContent = i
        newButton.addEventListener('click', function (event) {
            checkResult(event)
        })
        choiceButtons.append(newButton)
    }
}

function checkResult(event) {
    let button = event.target
    if (parseInt(event.target.textContent) === randomNumber){
        button.style.backgroundColor = 'green'
        result.textContent = 'Correct!'
    } else {
        button.style.backgroundColor = 'red'
        result.textContent = 'Try again.'
    }
}

startGameButton.addEventListener('click', generateButtons)
