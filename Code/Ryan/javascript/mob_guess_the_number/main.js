const app = new Vue ({
    el:'#app',
    data: {
        currentGuess: '',
        randomNumber: 0,
        message: '',
        counter: 0
    },
    created: function () {
        let number = Math.floor(Math.random() * 10 ) + 1
        this.randomNumber = number
    },
    methods: {
        newRandomNumber: function (){
            let number = Math.floor(Math.random() * 10 ) + 1
            this.randomNumber = number
            this.counter = 0
        },
        checkGuess: function (number) {
            this.counter +=1
            console.log(number)
            this.currentGuess = number
            if (this.currentGuess == this.randomNumber){
                this.message = 'Correct! You got it!'              
            } else {
                this.message = 'Incorrect, try again.'
            }
            this.currentGuess = ''
            if (this.message == 'Correct! You got it!'){
                newRandomNumber()
            }
        }

        
        // myMethod: function(text) {
        //     alert(text)
        // }
    }
})

// console.log(Math.random()) // random number between 0 and 1
// console.log(Math.random()*10) // random number between 0 and 20
// console.log(20 + Math.random()*20) // random number between 20 and 40
// console.log(Math.floor(20 + Math.random()*20)) // random *integer* between 20 and 40
// let letters = ['a', 'b', 'c']
// console.log(letters[Math.floor(Math.random()*letters.length)]) // random element

// function randint(a, b) {
//     return Math.floor(a + Math.random()*(b-a+1))
// }

// function randomChoice(arr) {
//     let i = randint(0, arr.length-1)
//     return arr[i]
// }

// let x = randint(1, 10) // a random number between 1 and 10
// console.log(x)