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

const cdInput = document.querySelector('#cd-input')
const units = document.querySelector('#units')
const cdBtn = document.querySelector('#cd-btn')
const cdTimer = document.querySelector('#cd-timer')

let cdInterval

function countdownTimer(){
    const cdTime = new Date()
    cdTime.setHours(0,0,0,0)
    if(units.value === 'seconds'){
        cdTime.setSeconds(cdInput.value-1)
    } else if (units.value === 'minutes'){
        cdTime.setMinutes(cdInput.value-1, 59)
    } else {
        cdTime.setHours(cdInput.value-1, 59, 59)
    }

    cdInput.value = ''

    cdTimer.textContent = cdTime.toLocaleTimeString('en-GB')
    if(cdInterval){
        clearInterval(cdInterval)
    }
    cdInterval = setInterval(function() {
        cdTime.setSeconds(cdTime.getSeconds() - 1)
        cdTimer.textContent = cdTime.toLocaleTimeString('en-GB')
        if(cdTime.getHours() === 0 && cdTime.getMinutes() === 0 && cdTime.getSeconds() === 0){
            clearInterval(cdInterval)
            alert('Times up!')
        }
    }, 1000)
}

cdBtn.addEventListener('click', countdownTimer)

const switchClock = document.querySelector('#switch-clock')
const switchStopwatch = document.querySelector('#switch-stopwatch')
const switchCountdown = document.querySelector('#switch-countdown')
const clockDiv = document.querySelector('#clock')
const stopwatchDiv = document.querySelector('#stopwatch-div')
const countdownDiv = document.querySelector('#countdown')

clockDiv.style.display = 'none'
stopwatchDiv.style.display = 'none'
countdownDiv.style.display = 'none'

switchClock.addEventListener('click', function(){
    clockDiv.style.display = 'block'
    stopwatchDiv.style.display = 'none'
    countdownDiv.style.display = 'none'
})

switchStopwatch.addEventListener('click', function(){
    clockDiv.style.display = 'none'
    stopwatchDiv.style.display = 'block'
    countdownDiv.style.display = 'none'
})

switchCountdown.addEventListener('click', function(){
    clockDiv.style.display = 'none'
    stopwatchDiv.style.display = 'none'
    countdownDiv.style.display = 'block'
})

