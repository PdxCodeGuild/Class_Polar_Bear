
const choices = ['Rock', 'Paper', 'Scissors']

const rockChoice = document.querySelector('#rock')
const paperChoice = document.querySelector('#paper')
const scissorsChoice = document.querySelector('#scissors')

let userChoice 
let compChoice
let gameResults

rockChoice.addEventListener('click', function () {
    let userChoice = 'Rock'
    playGame(userChoice)
})

paperChoice.addEventListener('click', function () {
    let userChoice = 'Paper'
    playGame(userChoice)
})


scissorsChoice.addEventListener('click', function () {
    let userChoice = 'Scissors'
    playGame(userChoice)
})

function playGame(userChoice) {
    let randChoice = Math.floor(Math.random() * choices.length)
    // console.log(choices[randChoice])
    // console.log(userChoice)
    let compChoice = choices[randChoice]
    let gameResults
    if (userChoice === compChoice) {
        gameResults = 'Tied'
        // console.log(gameResults)
    } else if (userChoice === 'Paper' && compChoice === 'Rock') {
        gameResults = 'You won'
        // console.log(gameResults)
    } else if (userChoice === 'Paper' && compChoice === 'Scissors') {
        gameResults = 'You lost'
        // console.log(gameResults)
    } else if (userChoice === 'Scissors' && compChoice === 'Paper') {
        gameResults = 'You won'
        // console.log(gameResults)
    } else if (userChoice === 'Scissors' && compChoice === 'Rock') {
        gameResults = 'You lost'
    } else if (userChoice === 'Rock' && compChoice === 'Paper') {
        gameResults = 'You lost'
        // console.log(gameResults)
    } else if (userChoice === 'Rock' && compChoice === 'Scissors') {
        gameResults = 'You won'
    } else { gameResults = 'not working' }
    // console.log(gameResults)}


    let gameOver = document.querySelector('#results')
    gameOver.textContent = `You chose ${userChoice} \nComputer chose ${compChoice}\nResults: ${gameResults}`
    // console.log(userChoice) 
}
