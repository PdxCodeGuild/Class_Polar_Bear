const app = new Vue ({
    el: '#app',
    data: {
        item: '',
        items: [],
        ids: [],
        id: '',
        status: ''
        
    },
    methods: {
        addItem: function () {
            let newItem = {text: this.item, completed:false, status:''}
            
            this.items.push(newItem)
            // this.completed.push(false)
            // console.log(this.items.indexOf(newItem))
            let index = this.items.indexOf(newItem)
            this.id = index
            // console.log(index)
            this.item = ''

        },
        lineThrough: function (index) {
            console.log(this.items[index].text)
            // with for loop you can bring in the index by passing it from html
            // set the item completed to toggle
            this.items[index].completed = !this.items[index].completed
            console.log(this.items[index].completed)
            // if item is completed then change status
            if (this.items[index].completed === true){
                this.items[index].status = 'line-through'
            } else {
                this.items[index].status = ''
            }



        },
        deleteItem: function (index) {
            console.log(index)
            // let index = this.items.indexOf(item)
            // console.log(index)
            this.items.splice(index, 1)
        }
    }
})