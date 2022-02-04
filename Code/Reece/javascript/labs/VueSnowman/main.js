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
        message: '',
        userWord: '',
        correctLetter: 0,
        attempts: 0,
        snowman: 'https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg',
    },
    methods: {
        checkLetter: function (letter, index) {
            console.log(letter)
            if (this.attempts < 8) {
                this
                for (let i = 0; i < app.word.length; i++){
                    if (letter === app.word[i]){
                        this.userWord += letter
                        this.correctLetter += 1
                    }
                }
            }
            else {
                console.log('game over')
            }
        },
        wordGeneration: function () {
            axios ({
                method: 'get',
                url: 'https://random-word-api.herokuapp.com/word/?swear=0',
            }).then(function (response) {
                app.word = response.data[0]
            })
        }
    },
    created () {
        this.wordGeneration()
    }

})