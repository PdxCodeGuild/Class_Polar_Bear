let userChoice = prompt("Please Enter Rock, Paper or Scissors")
// alert("Hello " + userChoice)
let computerChoice = Math.floor(Math.random()*2);
// console.log(computerChoice)
// alert(computerChoice)

if (computerChoice<=0)
{
    computerChoice ="rock"
}
else if ( computerChoice = 1)
{
    computerChoice ="paper"
}
else if ( computerChoice = 2)
{
    computerChoice ="scissors"
}

// let choice1,choice2
// let compare =function(choice1,choice2)
// {
// if( choice1 === choice2)
// {
//     alert("This is a tie")
// }
// }

if (userChoice == computerChoice)
{
    alert("This is a tie")   
}

else if(userChoice === "rock")
{
    if(computerChoice === "paper")
    {
        alert("The computer Wins!")
    } 
    else 
    {
        alert("You Win")

    }
}

else if (userChoice === "paper")
 {
    if (computerChoice === "scissors") 
    {
        alert("The computer Wins")
    } 
    else 
    {
        alert("You Win!")
    }
}

    
else if (userChoice === "scissors") 
{
        if (computerChoice === "rock") 
        {
            alert( "The computer wins")
        } 
        else 
        {
           alert("You win!")
         
        }
}


// console.log("user choice is : " + userChoice);
// console.log("computer choice: " + computerChoice)
// compare(userChoice,computerChoice)