const app = new Vue({
  el: "#app",
  data: {
    uppercase: 0,
    lowercase: 0,
    digits: 0,
    specialCharacters: 0,
    password: "",
    alphabetUpper :["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
    alphabetLower: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    alphabetDigits: [1,2,3,4,5,6,7,8,9],
    alphabetPunctuation: ['!', '#', '$', '%', '&', '(', ')', '*', '-', '<', '=', '>', '?', '@', '^', '_', '~'],
    temp : []
  },
  methods: {
    generateSegment: function(charCount, originArray ){
        const temp = []
          for (let i = 0; i < this.charCount; i++){
              const randomNum = Math.floor(Math.random() * originArray.length)
              temp.push(this.originArray[randomNum])
          }
      }
    },
    generatePassword: function () {
        if (this.uppercase){
            this.generateCharacters(this.uppercase, this.alphabetUpper)
        }
        
    },
    generateCharacters: function(){
        String.charCodeAt()
    }
  },
  created: function () {

  },
});
