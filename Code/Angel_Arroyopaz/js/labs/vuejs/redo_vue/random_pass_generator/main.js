const app = new Vue ({
    el: '#app',
    data: {
        userInputUpper: '',
        userInputLower: '',
        userInputDigits: '',
        userInputSpecial: '',
        alphabetUpper: ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
        alphabetLower: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        alphabetDigits: [1,2,3,4,5,6,7,8,9],
        alphabetPunctuation: ['!', '#', '$', '%', '&', '(', ')', '*', '-', '<', '=', '>', '?', '@', '^', '_', '~'],
        password: '',
    }, methods: {
        passwordGenerator: function () {
            let tempPassword = [];
            if (this.userInputUpper){
                for (let i=0 ; i<parseInt(this.userInputUpper) ; i++) {
                    randomNumber = Math.floor(Math.random() * 26);
                    tempPassword.push(this.alphabetUpper[randomNumber]);
                }
            }
            if (this.userInputLower){
                for (let i=0 ; i<parseInt(this.userInputLower) ; i++) {
                    randomNumber = Math.floor(Math.random() * 26);
                    tempPassword.push(this.alphabetLower[randomNumber]);
                }
            }
            if (this.userInputDigits){
                for (let i=0 ; i<parseInt(this.userInputDigits) ; i++) {
                    randomNumber = Math.floor(Math.random() * 9);
                    tempPassword.push(this.alphabetDigits[randomNumber]);
                }
            }
            if (this.userInputSpecial){
                for (let i=0 ; i<parseInt(this.userInputSpecial) ; i++) {
                    randomNumber = Math.floor(Math.random() * 17);
                    tempPassword.push(this.alphabetPunctuation[randomNumber]);
                }
            }

            tempPassword = this.shuffleFunction(tempPassword);
            tempPassword = tempPassword.join('');
            tempPassword = tempPassword.toString();
            this.password = tempPassword;

            this.userInputUpper = '';
            this.userInputLower = '';
            this.userInputDigits = '';
            this.userInputSpecial = '';
        } , 
        shuffleFunction: function (array) {
            let currentIndex = array.length,  randomIndex;
          
            // While there remain elements to shuffle...
            while (currentIndex != 0) {
          
              // Pick a remaining element...
              randomIndex = Math.floor(Math.random() * currentIndex);
              currentIndex--;
          
              // And swap it with the current element.
              [array[currentIndex], array[randomIndex]] = [
                array[randomIndex], array[currentIndex]];
            }
          
            return array;
          }
    }
})