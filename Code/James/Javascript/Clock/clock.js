/* Version 1 (clock): Code from https://www.w3schools.com/js/tryit.asp?filename=tryjs_timing_clock

onload=startTime()

function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s;
    setTimeout(startTime, 1000);
}
  
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

*/

// Version 2: Stopwatch. Used tutorial from https://codepen.io/cathydutton/pen/GBcvo   https://jsfiddle.net/Daniel_Hug/pvk6p/


//add const and function

const currentTime = document.querySelector('#current-time')

setInterval(function(){
    const date = new Date()
    currentTime.textContent = date.toLocaleTimeString('en-US')
}, 1000)

const startBtn = document.querySelector('#start')
const lapBtn = document.querySelector('#lap')
const stopBtn = document.querySelector('#stop')
const stopwatch = document.querySelector('#stopwatch')
const lapTimes = document.querySelector('#lap-times')

let stopwatchInterval
const swTime = new Date()

startBtn.addEventListener('click', function () {
    swTime.setHours(0,0,0,0)
    stopwatch.textContent = swTime.toLocaleTimeString('en-GB')
    lapTimes.innerHTML = ''
    startBtn.disabled = true
    if (stopwatchInterval) {
        clearInterval(stopwatchInterval)
    }
    stopwatchInterval = setInterval(function(){
        swTime.setSeconds(swTime.getSeconds() + 1)
        stopwatch.textContent = swTime.toLocaleTimeString('en-GB')
    }, 1000)
})

lapBtn.addEventListener('click', function(){
    if(stopwatchInterval){
        let li = document.createElement('li')
        li.textContent = swTime.toLocaleTimeString('en-GB')
        lapTimes.append(li)
    }
})

stopBtn.addEventListener('click', function(){
    startBtn.disabled = false
    if (stopwatchInterval) {
        clearInterval(stopwatchInterval)
    }
})

