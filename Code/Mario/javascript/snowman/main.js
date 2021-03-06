var app = vue({
  el: "#app",
  data: {
    blanks: "",
  },
  method: {
    createBlanks: function (secretWord) {
      for (char in secretWord) {
        this.blanks += "_";
      }
    },
  },
  created: {
    request: function () {
      url = "https://random-word-api.herokuapp.com/word/?swear=0";
      axios({
        method: "GET",
        url: url,
      }).then((data) => {
        //extract word from json and pass to createBlanks

        this.createBlanks("The cimb back");
      });
    },
  },
});

// ue Snowman
// Let's write a program to play a game of Snowman! Snowman is a word
// game where a secret word is chosen, then players have to guess letters
//  until they get the word correct or they run out of chances and lose.
// We can use <../docs/13%20-%20APIs%20and%20Ajax.md#ajax-in-axios|Axios>
// to send a request to this random word API.
// https://random-word-api.herokuapp.com/word/?swear=0

// Show them a list of 'blanks' and ask them for a letter.
// If they guess a letter which is in the word, show the blanks with the
// letters filled in. If they guess a letter which is not in the word,
// tell them and subtract 1 from their remaining guesses. Allow the user 10
//  tries to guess the letters of the word. If the… Show more
// <https://github.com/PdxCodeGuild/Class_Polar_Bear|PdxCodeGuild/Class_Polar_Bear>PdxCodeGuild/Class_Polar_Bear | Added by GitHub
