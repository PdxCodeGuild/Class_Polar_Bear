/*
Show them a list of 'blanks' and ask them for a letter. 
If they guess a letter which is in the word, show the blanks with the letters filled in. 
If they guess a letter which is not in the word, 
tell them and subtract 1 from their remaining guesses. 
Allow the user 10 tries to guess the letters of the word. 
If the user can't guess the word in the number of allotted guesses, 
print the word and ask them if they'd like to play again.

We could either have an input field and button for making a guess, 
or have a button for every letter and disable it after guessing.

For images, this page (https://www.hanginghyena.com/snowman) has a series of images that can be linked to.
Axios API: https://random-word-api.herokuapp.com/word/?swear=0 
*/


let app = new Vue ({
    el: '#app',
    data: {
        alphabet: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        word: '',
        message: '',
    },
    methods: {

/* If they guess a letter which is in the word, show the blanks with the letters filled in. 
If they guess a letter which is not in the word, 
tell them and subtract 1 from their remaining guesses. 
Allow the user 10 tries to guess the letters of the word.  */

/* Need to feed letters back into slots and fix logic bug - redo loops */
                
/* Need to insert "You win!" */           

/* Show them a list of 'blanks' and ask them for a letter. 
If the user can't guess the word in the number of allotted guesses, 
print the word and ask them if they'd like to play again. */

        reset: function () {
            this.message = '';
            this.randomWord(); 

/* We could either have an input field and button for making a guess, 
or have a button for every letter and disable it after guessing. */

/* Use Query Selectors */

/* Axios API: https://random-word-api.herokuapp.com/word/?swear=0 */

        randomWord: function () {
            axios ({
                method: 'get',
                url: 'https://random-word-api.herokuapp.com/word/?swear=0',
            }).then(function (response) {
                app.word = response.data[0]
            })
        }
        
/* Created for randomWord output */

    },
    created () {
        this.randomWord()
    }
})