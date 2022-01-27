var app = new Vue({
  el: "#app",
  data: {
    choices: ["ROCK", "PAPER", "SCISSORS"],
    result: ""
  },
  methods: {
    echoice: function (event) {
      const user = event.target.textContent
      const computer = this.rchoice()
      console.log(`Computer = ${computer} and User = ${user}`)

      if (user == computer) {
        this.result = `We both chose ${computer}.  TIE!`
      } else {
        if (user == this.choices[0]) {
          if (computer == this.choices[1]) {
            this.result = `You lose vs ${computer}.`
          } else {
            this.result = `You win vs ${computer}!`
          }
        }

        if (user == this.choices[1]) {
          if (computer == this.choices[2]) {
            this.result = `You lose vs ${computer}.`
          } else {
            this.result = `You win vs ${computer}!`
          }
        }

        if (user == this.choices[2]) {
          if (computer == this.choices[0]) {
            this.result = `You lose vs ${computer}.`
          } else {
            this.result = `You win vs ${computer}!`
          }
        }
      }
    },
    rchoice: function () {
      const randInt = Math.floor(Math.random() * this.choices.length);
      return this.choice[randInt]
    }
  }
}

