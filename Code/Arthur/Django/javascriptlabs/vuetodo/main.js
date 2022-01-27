var app = new Vue({
    el: '#app',
    data: {
        isEditing:false,
        selectedIndex: null,
        todo:'',
       todos : [
           'go to market',
           'buy new car',
       ]
        
    },
    methods: {

        storeTodo(){

            this.todos.push(this.todo)
            this.todo =''
        },

        editTodo(index,todo){
            this.todo=todo
            this.selectedIndex=index
            this.isEditing=true
        },

        updateTodo(){


            this.todos.splice(this.selectedIndex,1,this.todo)
            this.isEditing=false


        },

        deleteTodo(index){
            this.todos.splice(index,1)
        }

        
   
     

    },
    created: function() {

    }
})

