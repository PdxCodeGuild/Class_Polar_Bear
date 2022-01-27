
// Clock
const currentTime = document.querySelector('#current-time')

setInterval(function(){
    const date = new Date()
    currentTime.textContent = date.toLocaleTimeString('en-US')
}, 1000)

// Stopwatch
const startBtn = document.querySelector('#start')
const lapBtn = document.querySelector('#lap')
const stopBtn = document.querySelector('#stop')

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