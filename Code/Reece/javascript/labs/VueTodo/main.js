const app = new Vue ({
    el: '#app',
    data: {
        empty: [],
        todoInp: '',
        counter: 0,
        newValue: '',
    },
    created: function (){
    },
    methods: {
        // createTodo: function (){
        //     
        //     console.log(this.todoInp)
        //     console.log(this.counter)
        //     Vue.component(`todo${this.counter}`), {
        //         render: function (createElement) {
        //             return createElement(
        //                 'todo' + this.counter,
        //             )
        //         }
        //     }
        // },
        add: function(event){
            // this.counter += 1
            // this.item = [<input type="text"/>]
            this.empty.push(this.todoInp)
            console.log('test')
            this.newValue = this.todoInp
        }
    }
})