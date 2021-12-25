var app = new Vue({
    el: '#app',
    data: {
        newTodo: '',
        counter: 0,
        todoDivName: '',
        incTodoList: [],
        cmpTodoList: [],
        parent: '',
        
    },
    methods: {
        createTodo: function() {
            this.counter +=1
            if (this.newTodo !== ''){
                this.incTodoList.push(this.newTodo)
                this.todoDivName = 'todo' + this.counter
            }
            console.log(this.incTodoList)
        },
        moveTodo: function(event){
            this.parent= event.$root
        }
    },
    created: function() {

    }
})