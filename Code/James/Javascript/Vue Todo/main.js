const app = new Vue({
    el: '#app',
    data: {
        todoText: '',
        todoList: []
    },
    methods: {
        addTodo: function () {
            if (!this.todoText) return

            //if (!this.todoText) {
                //return
            //}
            this.todoList.push({text: this.todoText, completed:false})
            this.todoText =''
        },
        deleteTodo: function (index) {
            this.todoList.splice(index, 1)
        },
        completeTodo: function (index) {
            if (this.todoList[index].completed){
                this.todoList[index].completed = false 
            } else {
                this.todoList[index].completed = true
            }

            let completedList = todoList.filter(function (todo){
                return todo.completed
            })
            let uncompletedList = this.todoList.filter(function (todo){
                return !todo.completeTodo
            })
            this.todoList = uncompletedList.concat(completedList)
            console.log(todo.text)
        }
    }
})