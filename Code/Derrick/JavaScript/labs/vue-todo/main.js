const app = new Vue({
  el: "#app",
  data: {
    todos: [],
    newTodo: "",
  },
  methods: {
    addTodo: function () {
      this.todos.push({
        task: this.newTodo,
        isDone: false,
      });
      this.sortTodos();
      this.newTodo = "";
    },
    sortTodos: function () {
      this.todos = this.todos.sort((x, y) => {
        if (x.isDone === y.isDone) {
          return 0;
        } else if (x.isDone) {
          return 1;
        } else {
          return -1;
        }
      });
    },
    completeTodo: function (todo) {
      todo.isDone = !todo.isDone;
      this.sortTodos();
    },
    removeTodo: function (i) {
      this.todos.splice(i, 1);
    },
  },
});
