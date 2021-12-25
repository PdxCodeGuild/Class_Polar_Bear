
const rpsChoices = ['rock', 'paper', 'scissors']
let choiceButton = document.querySelector('#choice-button')

// choiceButton.addEventListener()

choiceButton.addEventListener('click', function (){
    let indexRand = Math.floor(Math.random() * rpsChoices.length)
    let compChoice = rpsChoices[indexRand]
    let userInput = document.querySelector('#user-input')
    let userChoice = userInput.value
    
    if (compChoice == userChoice){
        document.getElementById('game-result').innerHTML = `Tie! You chose ${userChoice} and tied with ${compChoice}.`
    } else if (compChoice == 'rock'){
        if (userChoice == 'paper'){
            document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
        } else {
            document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
        }
    } else if (compChoice == 'paper'){
        if (userChoice == 'rock'){
            document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
        } else {
            document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
        }
    } else {
        if (userChoice == 'rock'){
            document.getElementById('game-result').innerHTML = `Win! You chose ${userChoice} and beat ${compChoice}.`
        } else {
            document.getElementById('game-result').innerHTML = `Lose! You chose ${userChoice} and lost to ${compChoice}.`
        }
    }
})