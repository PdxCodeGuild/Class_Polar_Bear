const app = new Vue({
    el: '#app',
    data: {
        // 👍
        randomNumber: 0,
        message: '',
        counter: 0,
        userMax: 0
    },
    methods: {
        checkGuess: function (i) {
            this.counter += 1
            if (i == this.randomNumber){
                this.message = `Correct! You got it in ${this.counter} ${this.counter == 1 ? 'guess' : 'guesses'}. 😎`
                this.initializer()
            } else {
                this.message = "Incorrect, try again."
                let buttonId = document.querySelector(`#b${i}`)
                buttonId.disabled = true
            }
        },
        generateNumber: function () {
            // Generate random number between 1-10
            let number = Math.floor(Math.random() * this.userMax) + 1
            this.randomNumber = number
        },
        initializer: function () {
            for (let i = 1; i <= this.userMax; i++){
                document.querySelector(`#b${i}`).disabled = false // :)
            }
            this.generateNumber()
            this.counter = 0
        }
    }
})