const choiceInput = document.querySelector('#choice-input');
const choiceButton = document.querySelector('#choice-button');
const choices = ['rock', 'paper', 'scissors'];
let computerChoice = choices[Math.floor(Math.random() * 3)];

choiceInput.addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
    getResult()
  }
})

choiceButton.addEventListener('click', getResult);

function getResult() {
  let choice = choiceInput.value;

  if (choice !== 'rock' && choice !== 'paper' && choice !== 'scissors' && choice !== 'r' && choice !== 'p' && choice !== 's') {
    alert('Not a valid input');
  }
  if (choice === 'rock' && computerChoice === 'scissors') {
    result = 'You Win!'
  }
  else if (choice === 'paper' && computerChoice === 'rock') {
    result = 'You Win!'
  }
  else if (choice === 'scissors' && computerChoice === 'paper') {
    result = 'You Win!'
  }
  else if (computerChoice === 'rock' && choice === 'scissors') {
    result = 'Computer Wins :('
  }
  else if (computerChoice === 'paper' && choice === 'rock') {
    result = 'Computer Wins :('
  }
  else if (computerChoice === 'scissors' && choice === 'paper') {
    result = 'Computer Wins :('
  }
  else {
    result = 'Tie';
  }

  choice = '';
  let rpsResult = document.querySelector('#rps-result');
  rpsResult.textContent = result;
}