// Create Axios call with routes and call from a view

// App Template from Django JS Blog

const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Test',
        newsupplierid: '',
        newcapacity: '',
        newquality: '',
        newtimeliness: '',
        newcapacity_ave: '',
        newquality_ave: '',
        newtimeliness_ave: '',
        newitem_id: '',
        newitem_value: '',
        suppliers: []
    },
    methods: {
        submitSupplier: function () {
            const csrftoken = Cookies.get('csrftoken');
            console.log(csrftoken)
            axios({
                method: 'post',
                url: '../jsave_supplier/',
                headers: {'X-CSRFToken': csrftoken},
                data: {
                    supplierid: app.newsupplierid,
                    capacity: app.newcapacity,
                    quality: app.newquality,
                    timeliness: app.newtimeliness,
                    capacity_ave: app.newcapacity_ave,
                    quality_ave: app.newquality_ave,
                    timeliness_ave: app.newtimeliness_ave,
                    item_id: app.newitem_id,
                    item_value: app.newitem_value,
                }
            }).then(response => {
                app.getSuppliers()
                app.newsupplierid = ''
                app.newcapacity = ''
                app.newquality = ''
                app.newtimeliness = ''
                app.newcapacity_ave = ''
                app.newquality_ave = ''
                app.newtimeliness_ave = ''
                app.newitem_id = ''
                app.newitem_value = ''
                console.log(app.suppliers)
            })
        },
        getSuppliers: function () {
            axios({
                method: 'get',
                url: '../get_supplier/' 
            }).then(function (response) {
                app.suppliers = response.data.suppliers
                // Pass data into initMap function
                initMap(response.data.suppliers)
                console.log(app.suppliers)
            })
        }
    },
    created: function () {
        this.getSuppliers()
    }
})


function initMap(supplierdata) {
    // Create variable to pass in supplier data

    /*
    supplierdata 
    let obj = JSON.stringify(supplierdata)
    console.log(supplierdata)
    // First layer is JSON, second layer is an object
    console.log(supplierdata[0].capacity)
    let content1 = '<h2>Manufacturer</h2>'
    let imageRed = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
    let imageGreen = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
    let imageAmber = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
    // if (suppliderdata[0].capacity <5
*/
    
    

    // Map options (used https://youtu.be/Zxf1mnP5zcw Tutorial)
    var options = {
        zoom:8, 
        center:{lat:30.2672,lng:-97.7431}
    }

    // New map
    var map = new google.maps.Map(document.getElementById('map'), options);

    // Listen for click on map
    
    /*
    //Add marker
    var marker = new google.maps.Marker({
        position:{lat:30.2672,lng:-97.7431},
        map:map,
        icon:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
    });

    var infoWindow = new google.maps.InfoWindow({
        content:'<h1>Manufacturing Plant</h1>'
    });
    
    marker.addListener('click', function(){
        infoWindow.open(map,marker);
    });

    */

    // Array of markers (taken out: content: content1,)
    var markers = [
        {
            coords:{lat:30.2672,lng:-97.7491},
            iconImage:'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            content: '<h2>Manufacturer</h2>',
        },
        {
            coords:{lat:29.4241,lng:-98.4936},
            iconImage:'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
            content:'<h2>Supplier 1</h2>',
        },
        {
            coords:{lat:29.7066,lng:-96.5397},
            iconImage:'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            content:'<h2>Customer</h2>',
        },
        {
            coords:{lat:31.0982,lng:-97.3428},
            iconImage:'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            content:'<h2>Supplier 2</h2>',
        },
    ];

    // Loop through markers
    for(var i = 0;i < markers.length;i++){
        addMarker(markers[i]);
    }

    /* Old
    addMarker({
        coords:{lat:30.2672,lng:-97.7431},
        iconImage:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
        content:'<h2>Manufacturer</h2>'
    }); //Austin {lat:30.2672,lng:-97.7431}
    addMarker({
        coords:{lat:29.4241,lng:-98.4936},
        content:'<h2>Supplier 1</h2>'
    }); //San Antonio {lat:29.4241,lng:-98.4936}
    addMarker({coords:{lat:29.7066,lng:-96.5397}}); //Killeen {lat:29.7066,lng:-96.5397}
    addMarker({coords:{lat:31.0982,lng:-97.3428}}); //*Temple {lat:31.0982,lng:-97.3428}
    */

    // Add Marker Function
    function addMarker(props){
        var marker = new google.maps.Marker({
            position:props.coords, /* Austin is {lat:30.2672,lng:-97.7431}, */
            map:map,
            // icon:props.iconImage
        });

        // Check for custom icon
        if(props.iconImage){
            // Set icon image
            marker.setIcon(props.iconImage);
        }

        // Check content
        if(props.content){
            var infoWindow = new google.maps.InfoWindow({
                content:props.content
            });
            
            marker.addListener('click', function(){
                infoWindow.open(map,marker);
            });
        }
    };

    // Coordinates for Lines
    const sanAusCoordinates = [
        {lat:29.4241,lng:-98.4936},
        {lat:30.2672,lng:-97.7491},
    ];
    const temAusCoordinates =[
        {lat:31.0982,lng:-97.3428},
        {lat:30.2672,lng:-97.7491},
    ];
    const ausColCoordinates =[
        {lat:30.2672,lng:-97.7491},
        {lat:29.7066,lng:-96.5397},
    ];

    
    let colorYellow = "#F0FF33"
    let colorGreen = "#33FF36"
    let colorRed = "#FF0000"
    let colorBlack = "000000"


    // colorSanAusPath = '#FF0000'
    let x = supplierdata[0].capacity
    if (x < 3) {
        var colorSanAusPath = colorRed
    } else if (x < 8) {
        var colorSanAusPath = colorYellow
    } else if (x < 11) {
        var colorSanAusPath = colorGreen
    } else {
        var colorSanAusPath = colorBlack
    }
    

    // Add Paths         strokeColor: colorSanAusPath,
    const sanAusPath = new google.maps.Polyline({
        path: sanAusCoordinates,
        geodesic: true,
        strokeColor: colorSanAusPath,
        strokeOpacity: 1.0,
        strokeWeight: 6,
    });
    const temAusPath = new google.maps.Polyline({
        path: temAusCoordinates,
        geodesic: true,
        strokeColor: "#33FF36",
        strokeOpacity: 1.0,
        strokeWeight: 6,
      });
    const ausColPath = new google.maps.Polyline({
        path: ausColCoordinates,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 6,
        });
        // Set Maps
    temAusPath.setMap(map);
    sanAusPath.setMap(map);
    ausColPath.setMap(map);
}

/*
{lat:30.2672,lng:-97.7491}
{lat:29.4241,lng:-98.4936}
{lat:29.7066,lng:-96.5397}
{lat:31.0982,lng:-97.3428}
*/




