// our list of options
let list = ["rock", "paper", "scissors"]

// html tags
const rpsInput = document.querySelector('#rps-input')
const rpsButton = document.querySelector('#rps-button')

// create even listeners
rpsButton.addEventListener('click', rps)
rpsInput.addEventListener('keypress', function (event) {
    if (event.key === 'Enter'){
        rps()
    }
})


// function
function rps(){
    // random option
    let randIndex = Math.floor(Math.random() * list.length)
    let compChoice = list[randIndex]
    
    // tags values
    let userChoice = rpsInput.value

    userChoice = userChoice.toLowerCase()

    // define our empty result variable
    let result

    // main logic / comparison 
    if (userChoice === compChoice){
        result = 'Its a tie!'
    } else if (userChoice === 'rock'){
        if (compChoice === 'paper'){
            result = 'You lost!'
        } else if (compChoice === 'scissors'){
            result = 'You won!'
        } 
    } else if (userChoice === 'paper'){
        if (compChoice === 'scissors'){
            result = 'You lost!'
        } else if (compChoice === 'rock'){
            result = 'You won!'
        }
    } else if (userChoice === 'scissors'){
        if (compChoice === 'rock'){
            result = 'You lost!'
        } else if (compChoice === 'paper'){
            result = 'You won!'
        }
    }

    // clear our input text field and assigned the results to our h3 tag
    rpsInput.value = ''
    let rpsResult = document.querySelector('#rps-result')
    rpsResult.textContent = `${result} 
                            Computer:${compChoice} - You:${userChoice}`
}

