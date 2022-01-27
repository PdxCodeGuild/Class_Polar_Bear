const app = new Vue ({
    el: '#app',
    data: {
        guessLimit: 10,
        alphabet: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        word: '',
        warning: '',
    },
    methods: {
        checkGuess: function (i, buttonIndex) {
            if (this.guessLimit >= 1) {
                if (this.word.indexOf(i) > -1) {
                    document.querySelector(`#button${buttonIndex}`).className = "btn-close";
                    let index = this.word.indexOf(i);
                    while(index > -1) {
                        document.querySelector(`#wordPlace${index}`).textContent = i;
                        index = this.word.indexOf(i, index+1);
                    }

                } if (this.word.indexOf(i) < 0) {
                    this.guessLimit -= 1;
                    this.warning = `You have ${this.guessLimit} tries left!`;
                } 
            }
        },

        tryAgain: function () {
            this.ranWord();
            this.warning = '';
            this.guessLimit = 10;
            for (let i = 0; i < this.alphabet.length; i++) {
                document.querySelector(`#button${i}`).className = "btn btn-outline-info";
            }
            for (let i = 0; i < this.word.length; i++) {
                document.querySelector(`#wordPlace${i}`).textContent = "⍰";
            }
        },

        ranWord: function () {
            axios ({
                method: 'get',
                url: 'https://random-word-api.herokuapp.com/word/?swear=0',
            }).then(function (response) {
                app.word = response.data[0]
            })
        }

    },
    created () {
        this.ranWord()
    }
})