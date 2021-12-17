const app = new Vue({
  el: "#app",
  data: {
    word: "",
    counter: 10,
    guess: "",
    correct: "",
  },
  methods: {
    listenForKey: function () {
      window.addEventListener("keyup", function (event) {
        if (app.counter > 0) {
          app.counter--;
        }
        this.guess = event.key;
        let letters = document.querySelectorAll(".letter");
        letters.forEach((letter) => {
          if (letter.textContent === this.guess) {
            letter.classList.remove("hide");
            letter.classList.add("show");
            app.correct += this.guess;
          }
        });
        console.log(app.correct);
      });
    },
    resetWord: function () {
      this.counter = 10;
      this.guess = "";
      this.correct = "";
      let letters = document.querySelectorAll(".letter");
      letters.forEach((letter) => {
        letter.classList.remove("show");
        letter.classList.add("hide");
      });
      this.getNewWord();
    },
    getNewWord: function () {
      axios({
        method: "GET",
        url: "https://random-word-api.herokuapp.com/word/?number=7&swear=0",
      }).then(function (response) {
        app.word = response.data[0];
      });
    },
  },
  created() {
    this.getNewWord();
  },
  mounted() {
    this.listenForKey();
  },
});
