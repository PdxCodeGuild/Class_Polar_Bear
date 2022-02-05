// Let's write a program to play a game of Snowman! Snowman is a
//  word game where a secret word is chosen, then players have to
//   guess letters until they get the word correct or they run out
//    of chances and lose.

// We can use Axios to send a request to this random word API.

// https://random-word-api.herokuapp.com/word/?swear=0

// Show them a list of 'blanks' and ask them for a letter.
// If they guess a letter which is in the word,show the blanks 
// with the letters filled in. If they guess a letter which is 
// not in the word, tell them and subtract 1 from their
// remaining guesses. Allow the user 10 tries to guess the 
// letters of the word. If the user can't guess the word
// in the number of allotted guesses, print the word and 
// ask them if they'd like to play again.

// We could either have an input field and button for 
// making a guess, or have a button for every letter and disable it after guessing.

// For images, this page has a series of images that can be linked to.

const app = new Vue ({
    el: '#app',
    data: {
        letters: ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        word: '',
        attempts: 1,
        snowman: 'https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg',
    },
    methods: {
        checkLetter: function (letter, index) {
            // console.log(letter)
            // console.log(index)
            document.getElementById(`${letter}`).style.visibility='hidden'
            if (this.attempts < 7) {
                this.attempts +=1
                    // console.log(this.attempts, 'before subtraction')
                for (let i= 0; i <this.word.length; i ++){
                    if (letter === this.word[i]){
                        // console.log(i)
                        document.getElementById(`letter${i}`).textContent = `-_${letter}_-`
                        this.attempts -= 1
                        // console.log(this.attempts, 'after subtracting')
                    }
                }
                this.snowman = `https://www.hanginghyena.com/static/branding/art/Snowman-${this.attempts}.jpg`
            }
            else {
                alert('GAME OVER! Click okay to play again or exit the webpage.')
                this.snowman ='https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg'
                this.attempts = 1;
                this.wordGeneration();
                    for (let i = 0; i < this.letters.length; i ++){
                        letterValue = this.letters[i]
                        // console.log(letterValue)
                        document.getElementById(`${letterValue}`).style.visibility='visible'
                    }
                    for (let i = 0; i < this.word.length; i++){
                        newContent = ' _'
                        document.getElementById(`letter${i}`).textContent = '-___-'
                    }
            }
        },
        wordGeneration: function () {
            axios ({
                method: 'get',
                url: 'https://random-word-api.herokuapp.com/word/?swear=0',
            }).then(function (response) {
                app.word = response.data[0]
                console.log(app.word)
            })
        }
    },
    created () {
        this.wordGeneration()
    }

})