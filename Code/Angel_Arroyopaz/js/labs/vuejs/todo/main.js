const app = new Vue ({
    el: '#app',
    data: {
        userInput: '',
        myList: [],
    },
    methods: {
        // main function
        addTodo: function () {
            // append user input to myList array
            this.myList.push(this.userInput);
            this.userInput = '';
            return this.myList;
        },
        // function to remove li
        removeTodo: function (i) {
            document.querySelector(`#span${i}`).parentElement.remove();
        },
        // line through and move item to the bottom if completed  --- remove line through and move item to top if restored
        // change symbols and class name to target them with CSS
        completeTodo: function (i) {
            if (document.querySelector(`#bc${i}`).innerText === '✅') {
                document.querySelector(`#ul`).appendChild(document.querySelector(`#li${i}`));
                document.querySelector(`#bc${i}`).innerText = '↩️';
                document.querySelector(`#span${i}`).className = 'completed';
            } else {
                document.querySelector(`#ul`).insertBefore(document.querySelector(`#li${i}`), document.querySelector(`#ul`).firstChild);
                document.querySelector(`#bc${i}`).innerText = '✅';
                document.querySelector(`#span${i}`).className = 'restored';
            }

        }
    }
})