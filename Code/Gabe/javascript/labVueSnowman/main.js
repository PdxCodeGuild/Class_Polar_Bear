const app = new Vue({
  el: '#app',
  data: {
    word: '',
    renderedWord: [],
    pics: [
      'https://www.hanginghyena.com/static/branding/art/Snowman-1.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-2.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-3.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-4.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-5.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-6.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-7.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-8.jpg',
      'https://www.hanginghyena.com/static/branding/art/Snowman-END.jpg',
    ],
    winnerPic: 'https://www.hanginghyena.com/static/branding/art/Snowman-WIN.jpg',
    wrongCount: 0,
    correctCount: 0,
    alphabet: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  },
  created: function () {
    axios.get('https://random-word-api.herokuapp.com/word/?swear=0')
    .then(res => {
      this.word = res.data[0].toUpperCase();
      this.renderedWord = new Array(this.word.length).fill('_')
    })
    // .then(() => {
    //   app.renderedWord = new Array(app.word.length).fill('_')
    // })
    .catch(err => console.log(err));
  },
  methods: {
    letterPress: function (letter) {
      const list = document.getElementById('alphabetUL');
      if (this.wrongCount > 7) {
        list.remove();
        this.renderedWord = this.word;
        return;
      }
      if (this.word.indexOf(letter) > -1) {
        console.log(this.word)
        for (let i = 0; i < this.word.length; i++) {
          if (letter === this.word[i]) {
            this.renderedWord[i] = letter;
            this.correctCount++;
            this.wrongCount++;
            this.wrongCount--;
          }
        }
        this.renderedWord = this.renderedWord;
      } else {
        this.wrongCount++;
      }
      if (this.correctCount === this.word.length) {
        this.wrongCount = 0;
        this.pics = [this.winnerPic];
        list.remove();
      }
    }
  }
})