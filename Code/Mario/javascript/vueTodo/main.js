Vue.component("todo-text", {
  props: ["todo", "btnDelete", "btnComplete"],
  template: `
  <li>{{todo.text}}
  <button class=" col-6 col-md-4 delete-item btn">Delete</button></li>`,
});

var app = new Vue({
  el: "#app",
  data: {
    todoList: [{ text: "hello" }],
    newItem: "",
  },
  methods: {
    addItem: function () {
      console.log("hello");
      var text = this.newItem;
      var id = 1;
      var package = { text, id };
      this.todoList.push(package);
      this.newItem = "";
      console.log(this.todoList);
    },
  },
});
