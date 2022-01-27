
const rpsChoices = ['rock', 'paper', 'scissors']
let choiceButton = document.querySelector('#choice-button')
let userInput = document.querySelector('#user-input')

userInput.addEventListener('keypress', function (event){
    if (event.key === 'Enter'){
        getResults()
    }
})

choiceButton.addEventListener('click', getResults)

function getResults() {
    let indexRand = Math.floor(Math.random() * rpsChoices.length)
    let compChoice = rpsChoices[indexRand]
    let userChoice = userInput.value
    
    if (!rpsChoices.includes(userChoice)){
        alert('Please choose: rock, paper, or scissors')
    }
    else {
        if (compChoice == userChoice){
            document.getElementById('game-result').innerHTML = `Tie! You chose ${userChoice} and tied with ${compChoice}.`
        }
        else if (compChoice == 'rock'){
            if (userChoice == 'paper'){
                document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
            }
            else {
                document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
            }
        }
        else if (compChoice == 'paper'){
            if (userChoice == 'rock'){
                document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
            }
            else {
                document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
            }
        }
        else {
            if (userChoice == 'rock'){
                document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
            }
            else {
                document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
            }
        }
    }
}