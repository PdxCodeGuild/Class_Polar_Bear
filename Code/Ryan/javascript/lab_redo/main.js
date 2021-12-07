
const choices = ['Rock', 'Paper', 'Scissors']

const rockChoice = document.querySelector('#rock')
const paperChoice = document.querySelector('#paper')
const scissorsChoice = document.querySelector('#scissors')

let userChoice 
let compChoice
let gameResults

rockChoice.addEventListener('click', function () {
    //fix with pulling the click event
    userChoice = 'Rock'
    playGame()
})

paperChoice.addEventListener('click', function () {
    userChoice = 'Paper'
    playGame()
})


scissorsChoice.addEventListener('click', function () {
    userChoice = 'Scissors'
    playGame()
})

function playGame() {
    let randChoice = Math.floor(Math.random() * choices.length)
    // console.log(choices[randChoice])
    // console.log(userChoice)
    let compChoice = choices[randChoice]
    // let gameResults
    if (userChoice === compChoice) {
        gameResults = 'Tied'
        // console.log(gameResults)
    } else if (userChoice === 'Paper') {
        if (compChoice === 'Rock'){
            gameResults = 'You won'
        } else {
            gameResults = 'You lost'
        } 
    // && compChoice === 'Rock') {
    //     gameResults = 'You won'
    //     // console.log(gameResults)
    // } 
    // else if (userChoice === 'Paper' && compChoice === 'Scissors') {
    //     gameResults = 'You lost'
    //     // console.log(gameResults)
    } else if (userChoice === 'Scissors') {
        if (compChoice === 'Paper') {
            gameResults = 'You won'
        } else {
            gameResults = 'You lost'
        }

    // } && compChoice === 'Paper') {
    //     gameResults = 'You won'
    //     // console.log(gameResults)
    // } else if (userChoice === 'Scissors' && compChoice === 'Rock') {
    //     gameResults = 'You lost'
    } else if (userChoice === 'Rock') {
        if (compChoice === 'Paper'){
            gameResults = 'You lost'
        } else {
            gameResults = 'You won'
        }
    // } && compChoice === 'Paper') {
    //     gameResults = 'You lost'
    //     // console.log(gameResults)
    // } else if (userChoice === 'Rock' && compChoice === 'Scissors') {
    //     gameResults = 'You won'
    } else { gameResults = 'not working' }
    // console.log(gameResults)}

    // document.createElement('p')
    let gameOver = document.querySelector('#results')
    gameOver.textContent = `You chose ${userChoice} \nComputer chose ${compChoice}\nResults: ${gameResults}`
    // console.log(userChoice) 
}
