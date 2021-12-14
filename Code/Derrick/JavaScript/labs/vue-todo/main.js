const app = new Vue({
  el: "#app",
  data: {
    todos: [],
    todoToAdd: "",
  },
  methods: {
    getTodo: function () {
      this.todos.push(this.todoToAdd);
      this.todoToAdd = null;
    },
    completeTodo: function (i, event) {
      const todoText = event.target.closest(".todo-item").firstChild.firstChild;

      if (todoText.style.textDecoration === "line-through") {
        todoText.style.textDecoration = "none";
      } else {
        todoText.style.textDecoration = "line-through";
      }
      console.log(todoText);
    },
    removeTodo: function (i) {
      this.todos.splice(i, 1);
    },
  },
});
