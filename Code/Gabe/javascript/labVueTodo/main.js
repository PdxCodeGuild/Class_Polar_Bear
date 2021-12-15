const app = new Vue({
  el: '#app',
  data: {
    message: '',
    todoInput: '',
    todos: [],
    completedTodos: []
  },
  methods: {
    addTodos: function() {
      if (this.todos.indexOf(this.todoInput) === -1 && this.todoInput !== '') {
        this.todos.push(this.todoInput);
        this.todoInput = '';
        this.message = '';
      } else
      if (this.todoInput === '') {
        this.message = 'Nothing to add';
      } else {
        this.message = 'Already on the list';
      }
    },
    complete: function(todo) {
      let index = this.todos.indexOf(todo);
      this.completedTodos.push(todo);
      this.todos.splice(index, 1);
    },
    deleteTodo: function (todo) {
      let indexTodo = this.todos.indexOf(todo);
      let indexComplete = this.completedTodos.indexOf(todo);
      if (indexTodo !== -1) {
        this.todos.splice(indexTodo, 1);
      }
      if (indexComplete !== -1) {
        this.completedTodos.splice(indexComplete, 1);
      }
    },
    returnTodo: function(todo) {
      this.todos.push(todo);
      this.completedTodos.splice(this.completedTodos.indexOf(todo), 1);
    }
  }
})

