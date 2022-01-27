const app = new Vue({
  created: function () {
    axios.get('https://randomwordgenerator.com/noun.php').then(res => {
      this.word = res.data[0];
    }).catch(err => console.log(err));
  },
  data: {
    count: 0,
    word: ''
  },
  el: '#app',
  methods: {
    letterChoice: function (letter) {
      if (this.word.indexOf(letter) > -1) {
        console.log(this.word)
        for (let i = 0; i < this.word.length; i++) {
          if (letter === this.word[i]) {
            this.count++;
          }
        }
    }
  }
})

