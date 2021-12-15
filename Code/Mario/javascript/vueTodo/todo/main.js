// Vue.component("todo-text", {
//   props: ["todo", "btnDelete", "btnComplete"],
//   template: `
//   <li>{{todo.text}}
//   <button id="deleteBtn" class=" col-3 col-md-2 delete-item btn">Delete</button>
//   <button id="doneBtn" class=" col-3 col-md-2 delete-item btn">Done</button>
//   </li>`,
// });

var app = new Vue({
  el: "#app",
  data: {
    todoList: [],
    newItem: "",
    id: 0,
    isCompleted: false,
  },
  methods: {
    addItem: function () {
      console.log("hello");
      var text = this.newItem;
      var id = this.id;
      this.id++;
      var status = this.isCompleted;
      var package = { text, id, status };
      this.todoList.push(package);
      this.newItem = "";
      // this.isCompleted = false;
    },
    updateItem: function (btnType, item) {
      for (i in this.todoList) {
        if (btnType == "doneBtn" && this.todoList[i].id == item.id) {
          this.todoList[i].status = true;
        } else if (btnType == "deleteBtn" && this.todoList[i].id == item.id) {
          this.todoList.splice(i, 1);
        }
      }
    },
  },
});
