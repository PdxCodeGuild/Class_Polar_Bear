const app = new Vue({
    el: '#app',
    data: {
        uppercase: '',
        lowercase: '',
        digits: '',
        specialCharacters: '',
        password: '',
        alphabetUpper: ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
        alphabetLower: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        alphabetDigits: [1,2,3,4,5,6,7,8,9],
        alphabetPunctuation: ['!', '#', '$', '%', '&', '(', ')', '*', '-', '<', '=', '>', '?', '@', '^', '_', '~'],
        temp: []
    },
    methods: {
        generateSegment: function (count, originArray) {
            for (let i = 0; i < count; i++){
                const randomNum = Math.floor(Math.random() * originArray.length)
                this.temp.push(originArray[randomNum])
            }
        },
        generatePassword: function () {
            if (this.uppercase) {
                this.generateSegment(this.uppercase, this.alphabetUpper)
            }
            if (this.lowercase) {
                this.generateSegment(this.lowercase, this.alphabetLower)
            }
            if (this.digits) {
                this.generateSegment(this.digits, this.alphabetDigits)
            }
            if (this.specialCharacters) {
                this.generateSegment(this.specialCharacters, this.alphabetPunctuation)
            }

            this.temp = this.shuffleArray(this.temp)

            this.password = this.temp.join('')
            this.uppercase = ''
            this.lowercase = ''
            this.digits = ''
            this.specialCharacters = ''

            this.temp = []
        },
        shuffleArray: function (array) {
            for (let i = 0; i < array.length; i++){
                const j = Math.floor(Math.random() * array.length)
                let temp = array[i]
                array[i] = array[j]
                array[j] = temp
            }

            return array
        }
    },
    created: function() {

    }
})