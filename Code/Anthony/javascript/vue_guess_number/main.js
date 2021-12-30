const app = new Vue({
    el: '#app',
    data: {
        currentGuess: '',
        randomNumber: 0,
        message: ''
    },
    created: function () {
        // Generate random number between 1-10
        let number = Math.floor(Math.random() * 10) + 1
        this.randomNumber = number
    },
    methods: {
        checkGuess: function () {
            if (this.currentGuess == this.randomNumber){
                this.message = "Correct! You got it!"
            } else {
                this.message = "Incorrect, try again."
            }
            this.currentGuess = ''
        }
    }
})