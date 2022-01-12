let app = new Vue({
          
    el: '#app',
    
    data: {
      snowman_images: [
          "https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-2.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-3.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-4.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-5.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-6.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-7.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-8.jpg",
          "https://www.hanginghyena.com/static/branding/art/Snowman-END.jpg"
      ],
      alphabet: "abcdefghijklmnoprstuvwxyz".split(''), // alphabet to generate buttons
      secret_word: '', // secret word that the user is guessing
      underscores: [], // underscores that are filled in each guess
      disabled: [], 
      num_guesses: 0, // number of guesses
      message: 'Playing Snowman!'
    },
    
    methods: {
      guessLetter: function(index) {
          // get the letter for the button that was pressed
          const letter = this.alphabet[index]
          this.disabled[index] = true
          console.log('Checking letter: ' + letter)
          //set flag to check if a letter is found in the for loop
          let found = false
          // iterate over the secret word
          for(let i=0; i< this.secret_word.length; ++i){
              // check if the letter matches the character of secret word at the given index
              // if it does match, replace the corresponding element in 'underscores' with that letter
              if(this.secret_word[i] === letter){
                  this.underscores[i] = letter
                  found = true
              }
          }
          // if letter not found in for loop, iterate num_guesses
          if (!found){
              this.num_guesses++

              //LOSE CONDITION

              //if number of guesses is greater than snowman images, game over
              if (this.num_guesses >= this.snowman_images.length - 1){
                  // this.disabled.fill(true)
                  for(let r=0; r < this.disabled.length; r++){
                      this.disabled[r] = true
                  }
                  this.message = `Bummer! The word was ${this.secret_word}`
              }
          }
          this.checkWin()
          this.$forceUpdate()
      },
      //start/restart game function
      startGame: function () {
          axios.get('https://random-word-api.herokuapp.com/word/?swear=0')
          .then((response) => {
             console.log(response.data) 
             this.secret_word = response.data[0]
             let new_arr = Array(this.secret_word.length).fill('_')
             this.disabled = Array(this.alphabet.length).fill(false)
          //    let new_arr = []
          //    for (let i=0; i<this.secret_word.length; i++) {
          //        new_arr.push('_')
          //    }
             this.underscores = new_arr
             this.num_guesses = 0
             this.message = "Playing SnowBody!"
        })
      },
      checkWin: function () {
          // convert underscores array into string
          const underscore_string = this.underscores.join('')
          // console.log(underscore_string)
          if (underscore_string === this.secret_word){
              //we win
              this.message = "YOU WIN!"
          }
      }
    },
    
    
    created: function() {
        this.startGame()
    }
  })