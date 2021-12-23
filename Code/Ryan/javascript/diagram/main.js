const draw = new Vue({
    el: '#input',
    data: {
        asset: '',
        assets: [],
        assetType: {'src': '', 'id': ''},
        i: 0

    },
    methods: {
        addAsset: function(){
            this.assets.push(this.asset)
            this.asset = ''
        },
        addContainer: function () {
            // this.asset = 'did if work'
            // console.log(this.asset)
            // let number = i
            this.i ++
            let newContainerName = document.createElement('input')
            newContainerName.addEventListener('change', newContainerName)
            newContainerName.type = 'text'
            newContainerName.id = `${this.i}`
            console.log(newContainerName)
            let c = document.getElementById("myCanvas")
            let ctx = c.getContext("2d")
            ctx.fillStyle = '#FF0000'
            ctx.fillRect(0, 0, 150, 100)
        },
        addAssetType: function(id){
            let c = document.getElementById("myCanvas")
            let ctx = c.getContext("2d")
            let name = id.srcElement.id
            let img = document.getElementById(name)
            console.log(id.srcElement.id)
            // console.log(img)
            // console.log(id)
            // console.log(id.srcElement)
            ctx.drawImage(img, 10, 10)
            // console.log(this.assetType)
            // this.assetType.push()
            // document.getElementById("scream");
        },
        removeAsset: function(asset) {
            let index = this.assets.indexOf(asset)
            this.assets.splice(index, 1)
        },

    }
})