
function dateTime() {

    // get current date
    const data = new Date();

    // get date
    let day = data.getDate();
    let mnt = data.getMonth() + 1;
    let yrs = data.getFullYear();

    // add date to DOM
    document.getElementById('DATE').innerHTML = 'Current Date: ' + day + '-' + mnt + '-' + yrs ;

    // get date
    let hrs = data.getHours();
    let min = data.getMinutes();
    let scs = data.getSeconds();

    // add time to DOM
    document.getElementById('time').innerHTML = 'Current Time: ' + hrs + ':' + min + ':' + scs;
}

// get current date
let swData = new Date();

// Create Reset Time (RS)
swData.setHours(0,0,0,0)

//get RS
let swHrs = swData.getHours();
let swMin = swData.getMinutes();
let swScs = swData.getSeconds();

const lapBtn = document.querySelector('#lap-btn')

function stopwatch(){

    // Count Seconds
    swScs += 1

    // Transfer to minutes
    if (swScs > 59){
        swScs -= 60;
        swMin += 1
    }

    //Transfer to hours
    if (swMin > 59){
        swScs -= 60;
        swMin += 1;
    }

    // add combine RS and add to DOM
    let swTime = swHrs + ':' + swMin + ':' + swScs;

    // Update DOM
    document.getElementById('stopwatch-time').innerHTML = swTime
}
 let counter = 0
lapBtn.addEventListener('click', function(){
    counter += 1
    let lapTime = document.getElementById('stopwatch-time').innerHTML
    let lap = document.createElement(`li`)
    lap.innerHTML = `Lap ${counter} = ` + lapTime
    let lapList = document.querySelector('#lap-list')
    lapList.appendChild(lap)
})

setInterval(dateTime, 1)

const startBtn = document.querySelector('#start-btn')

startBtn.addEventListener('click', function(){
    setInterval(stopwatch, 1000)
})