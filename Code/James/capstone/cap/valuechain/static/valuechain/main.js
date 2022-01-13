// Create Axios call with routes and call from a view

function initMap() {
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

    // Array of markers
    var markers = [
        {
            coords:{lat:30.2672,lng:-97.7431},
            iconImage:'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
            content:'<h2>Manufacturer</h2>',
        },
        {
            coords:{lat:29.4241,lng:-98.4936},
            content:'<h2>Supplier 1</h2>',
        },
        {
            coords:{lat:29.7066,lng:-96.5397},
            content:'<h2>Supplier 2</h2>',
        },
        {
            coords:{lat:31.0982,lng:-97.3428},
            content:'<h2>Customer</h2>',
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
    }
}