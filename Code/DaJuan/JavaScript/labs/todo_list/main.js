// const body = document.getElementById("body")
// const selection = document.getElementById("todo-input").innerHTML
// const inputBtn = document.getElementById("input-btn") = (selection) => {
//     addEventListener("click")
// }

const entry = new Vue({
    el: '#entry',
    data: {
        task: "",
        tasks: []
    },
    methods: {
        addTask: function () {this.tasks.push(this.task); this.task = ''},
        removeTask: function (task) {
            let index = this.tasks.indexOf(task)
            this.tasks.splice(index, 1),
            app.data.tasks.push(this.task)},
        markDone: () => {}
    }
})