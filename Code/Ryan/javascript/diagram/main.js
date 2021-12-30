const draw = new Vue({
    el: '#input',
    data: {
        asset: '',
        assets: [],
        assetType: {}
    },
    methods: {
        addAsset: function(){
            this.assets.push(this.asset)
            this.asset = ''
        },
        addAssetType: function(){
            
            console.log(assetType)
            // this.assetType.push()
        },
        removeAsset: function(asset) {
            let index = this.assets.indexOf(asset)
            this.assets.splice(index, 1)
        }
    }
})