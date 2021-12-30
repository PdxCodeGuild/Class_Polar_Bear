const app = new Vue({
  el: '#app',
  data: {
    currentGuess: '',
    randomNumber: 0,
    message: ''
  },
  created: function() {
    const number = Math.floor(Math.random() * 10) + 1;
    this.randomNumber = number;
  },
  methods: {
    checkGuess: function() {
      if (parseInt(this.currentGuess) === this.randomNumber) {
        this.message = 'Correct!'
      } else {
        this.message = 'incorrect'
      }
    }
  }
})