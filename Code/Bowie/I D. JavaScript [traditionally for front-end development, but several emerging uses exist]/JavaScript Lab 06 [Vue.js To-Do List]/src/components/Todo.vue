<template>
  <div class="container">
    <b-list-group>
      <b-list-group-item>
        <h2 class="mb-3">To-Do / Pour Faire List (with / avec Vue)</h2>
        <b-input-group class="my-3">
          <button class="btn btn-success" v-on:click="e => addTodo(e, newTodo)">Add / Adjouter</button>
          <b-form-input id="addTodo-input" placeholder="Type a to-do item here / Typer quelquechose pour faire ici:" v-model="newTodo"></b-form-input>
        </b-input-group>
      </b-list-group-item>
      <b-list-group-item class="py-3 d-flex justify-content-between align-items-center" v-for="todo in todos"
                         :key="todo.id" v-bind:class="{'todo-completed': todo.completed}" >
        {{todo.value}}
        <div v-show="!todo.completed">
          <b-button variant="primary" class="mx-2" v-on:click="() => completeTodo(todo.id)">That's finished / C'est fini</b-button>
          <b-button variant="danger" v-on:click="() => deleteTodo(todo.id)">Remove / Effacer</b-button>
        </div>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  data: () => ({
    todos: [],
    newTodo: '',
    id: 1
  }),
  methods: {
    addTodo: function(e, newTodoText) {
      newTodoText = newTodoText.trim();
      if(newTodoText) {
        this.todos = [...this.todos, {id: this.id, completed: false, value: newTodoText}];
        this.id++;
        this.newTodo = '';
      }
    },
    completeTodo: function(todoId) {
      let otherTodos = this.todos.filter(todo => todo.id !== todoId);
      let thisTodo = this.todos.filter(todo => todo.id === todoId)[0];
      thisTodo.completed = true;
      this.todos = [...otherTodos, thisTodo];
    },
    deleteTodo: function(todoId) {
      this.todos = this.todos.filter(todo => todo.id !== todoId);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.todo-completed {
  text-decoration: line-through;
}
</style>
