const app = new Vue ({
    el: '#app',
    data: {
        tinput: '',
        tlist: []
    },
    methods: {
        add_to_list: function () {
            this.tlist.push(this.tinput);
            this.tinput = '';
            return this.tlist;
        },
        complete_item: function (i) {
            if (document.querySelector(`#bc${i}`).innerText === 'ONE') {
                document.querySelector(`#ul`).appendChild(document.querySelector(`#li${i}`));
                document.querySelector(`#bc${i}`).innerText = 'TWO';
                document.querySelector(`#span${i}`).className = 'completed';
            }
        },
	remove_item: function (i) {
            document.querySelector(`#span${i}`).parentElement.remove();
        }
    }
})

