// our list of options
let list = ["rock", "paper", "scissors"]

// prompt
let userChoice = prompt('Choose an option!(rock, paper, or scissors):')

// random option
let randIndex = Math.floor(Math.random() * list.length)
let compChoice = list[randIndex]

// convert user input to lower case
userChoice = userChoice.toLowerCase()

// main logic / comparison 
if (userChoice === compChoice){
    alert(`Its a tie!. 
    Computer: ${compChoice} - You: ${userChoice}`)
} else if (userChoice === 'rock'){
    if (compChoice === 'paper'){
        alert(`You lost!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    } else if (compChoice === 'scissors'){
        alert(`You won!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    } 
} else if (userChoice === 'paper'){
    if (compChoice === 'scissors'){
        alert(`You lost!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    } else if (compChoice === 'rock'){
        alert(`You won!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    }
} else if (userChoice === 'scissors'){
    if (compChoice === 'rock'){
        alert(`You lost!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    } else if (compChoice === 'paper'){
        alert(`You won!. 
        Computer: ${compChoice} - You: ${userChoice}`)
    }
}


