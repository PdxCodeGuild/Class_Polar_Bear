// var app = new Vue({
//     el: '#app',
//     data: {
//         message: 'Hello Vue!',
//         newMe :'Test the waters!'
//     },
//     methods: {

//     },
//     created: function() {

//     }
// })
const choices = ["rock", "paper", "scissors"]
var app = new Vue({
    el: '#app',
    data: {
        
           userSelection: "",
           computerSelection: "",
           
        
       
    },
    computed: {
        result() {
            const { computerSelection, userSelection } = this
            if (computerSelection === userSelection) {
                return `it's a tie`
            } else {
                if (
                    (computerSelection === "rock" && userSelection === "scissors") ||
                    (computerSelection === "paper" && userSelection === "rock") ||
                    (computerSelection === "scissors" && userSelection === "paper")
                    ) {
                        return "computer wins"
                    }
                    return "You win"
                }
            },
        },
    methods: {
        play:function()
        {
            if (!this.userSelection) 
            {
                return
            }
            const computerChoiceIndex = Math.floor(Math.random() * choices.length)
            this.computerSelection = choices[computerChoiceIndex]
          },

    },
})

