
let startGameButton = document.querySelector('#start-game-button')
let choiceButtons = document.querySelector('#choice-buttons')
let result = document.querySelector('#result')

function generateButtons() {
    choiceButtons.innerHTML= ''
    result.textContent = ''
    let difficultyLevel = document.querySelector('#difficulty-level')
    let maxGuess = parseInt(difficultyLevel.value)
    let randomNumber = Math.floor(Math.random() * maxGuess) + 1

    for (let i = 1; i <= maxGuess; i++ ){
        let newButton = document.createElement('button')
        newButton.textContent = i
        newButton.addEventListener('click', function () {
            let button = event.target
            if (parseInt(event.target.textContent) === randomNumber){
                button.style.backgroundColor = 'green'
                result.textContent = 'Correct!'
            } else {
                button.style.backgroundColor = 'red'
                result.textContent = 'Try again.'
            }
        })
        choiceButtons.append(newButton)
    }
}

startGameButton.addEventListener('click', generateButtons)