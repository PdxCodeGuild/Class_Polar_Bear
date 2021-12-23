const app = new Vue({
  el: '#app',
  data: {
    uppercase: 0,
    lowercase: 0,
    digits: 0,
    specialChars: 0,
    password: '',
    uppercaseLetters: ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
    lowercaseLetters: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    digitsCharacters: [1,2,3,4,5,6,7,8,9],
    specialCharacters: ['!', '#', '$', '%', '&', '(', ')', '*', '-', '<', '=', '>', '?', '@', '^', '_', '~'],
    temp: []
  },
  methods: {
    generateSegment: function (count, originArray) {
      for (let i = 0; i < count; i++) {
        const randomNum = Math.floor(Math.random() * originArray.length);
        console.log(randomNum)
        this.temp.push(originArray[randomNum]);
      }
    },
    shuffleChars: function (a) {
      var j, x, i;
      for (i = a.length - 1; i > 0; i--) {
          j = Math.floor(Math.random() * (i + 1));
          x = a[i];
          a[i] = a[j];
          a[j] = x;
      }
      return a;
    },
    generatePassword: function () {
      if (this.uppercase) {
        this.generateSegment(this.uppercase, this.uppercaseLetters);
      }
      if (this.lowercase) {
        this.generateSegment(this.lowercase, this.lowercaseLetters);
      }
      if (this.digits) {
        this.generateSegment(this.digits, this.digitsCharacters);
      }
      if (this.specialChars) {
        this.generateSegment(this.specialChars, this.specialCharacters);
      }
      this.temp = this.shuffleChars(this.temp);
      this.password = this.temp.join('');
      this.temp = [];
    },
    clearPassword: function () {
      this.password = '';
    }
  }
})