var app = new Vue({
  el: "#app",
  data: {
    name: "Rock, Paper, Scissors!",
    choices: ["🗿", "📃", "✂️"],
    outcome: "",
  },
  methods: {
    randomChoice: function () {
      const randInt = Math.floor(Math.random() * this.choices.length);
      const randChoice = this.choices[randInt];
      return randChoice;
    },
    choice: function (event) {
      const userChoice = event.target.textContent;
      const computerChoice = this.randomChoice();
      console.log(`Computer: ${computerChoice} | User: ${userChoice}`);

      // Tie
      if (userChoice == computerChoice) {
        this.outcome = `We both chose ${computerChoice}.  TIE!`;
      } else {
        // User chooses Rock //
        if (userChoice == this.choices[0]) {
          if (computerChoice == this.choices[1]) {
            this.outcome = `I chose ${computerChoice}.  You lose.`;
          } else {
            this.outcome = `I chose ${computerChoice}.  You win!`;
          }
        }

        // User chooses Paper //
        if (userChoice == this.choices[1]) {
          if (computerChoice == this.choices[2]) {
            this.outcome = `I chose ${computerChoice}.  You lose.`;
          } else {
            this.outcome = `I chose ${computerChoice}.  You win!`;
          }
        }

        // User chooses scissors //
        if (userChoice == this.choices[2]) {
          if (computerChoice == this.choices[0]) {
            this.outcome = `I chose ${computerChoice}.  You lose.`;
          } else {
            this.outcome = `I chose ${computerChoice}.  You win!`;
          }
        }
      }
    },
  },
});
