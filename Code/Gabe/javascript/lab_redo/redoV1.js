
while (true) {
  const userInput = prompt("Welcome to RPS!! \n Enter 'rock' 'paper' or 'scissors \n enter done if you are finished");
  const choices = ['rock', 'paper', 'scissors'];
  let computerChoice = choices[Math.floor(Math.random() * 3)];

  if (userInput === 'done' && userInput === 'd') {
    break;
  }
  if (userInput !== 'rock' && userInput !== 'paper' && userInput !== 'scissors' && userInput !== 'r' && userInput !== 'p' && userInput !== 's') {
    alert('Not a valid input. Please refresh page to try again.');
    break;
  }
  if (userInput === 'rock' && computerChoice === 'scissors') {
    alert('You Win');
  }
  else if (userInput === 'paper' && computerChoice === 'rock') {
    alert('You Win');
  }
  else if (userInput === 'scissors' && computerChoice === 'paper') {
    alert('You Win');
  }
  else if (computerChoice === 'rock' && userInput === 'scissors') {
    alert('Computer Wins');
  }
  else if (computerChoice === 'paper' && userInput === 'rock') {
    alert('Computer Wins');
  }
  else if (computerChoice === 'scissors' && userInput === 'paper') {
    alert('Computer Wins');
  }
  else {
    alert('Tie!');
  }
}


