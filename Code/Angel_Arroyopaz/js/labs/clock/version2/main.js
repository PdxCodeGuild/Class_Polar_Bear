// declare variables and access html elements 
const startButton =  document.querySelector('#start-button');
const lapButton = document.querySelector('#lap-button');
const stopButton = document.querySelector('#stop-button');
const resetButton = document.querySelector('#reset-button');
const clock = document.querySelector('#clock');
const list = document.querySelector('#list');

let hr = 0;
let mnt = 0;
let secs = 0;
let miliSecs = 0;

let stopTime = false;
let counter = 1;

let timeInterval; 
let intervalOn = false;

// functions
// start
function stopWatchStart() {
    if (stopTime === false) {
        clock.innerHTML = hr + ':' + mnt + ':' + secs + ':' + miliSecs;
        secs++

        if (secs === 60) {
            mnt += 1;
            secs = 0;
        }

        if (mnt === 60) {
            hr += 1;
            mnt = 0
        }
    } 
}

// stop
function stopWatchStop() {
    intervalOn = false;
    stopTime = true;
}

// reset
function stopWatchReset() {
    intervalOn = false;
    hr = 0;
    mnt = 0;
    secs = 0;
    miliSecs = 0;
    clock.innerHTML = hr + ':' + mnt + ':' + secs + ':' + miliSecs;
    stopTime = false;
    counter = 1;
    while (list.firstChild) {
        list.removeChild(list.firstChild);
      }
}

// lap
function stopWatchLap() {
    if (stopTime === false && (hr + mnt + secs + miliSecs) > 0) {
        let li = document.createElement('li')
        li.innerHTML = 'Lap' + counter + ' ' + hr + ':' + mnt + ':' + secs + ':' + miliSecs;
        list.append(li)
        li.style.listStyleType = 'none';
        counter += 1;
    }
}


// event listeners for my buttons
startButton.addEventListener('click', function () {
    if (intervalOn === true) {
        console.log(intervalOn);
    } else {
        intervalOn = true;
        timeInterval = setInterval(stopWatchStart, 1000);
    }
})


lapButton.addEventListener('click', stopWatchLap)

stopButton.addEventListener('click', function () {
    clearInterval(timeInterval);
    stopWatchStop();
})

resetButton.addEventListener('click', function () {
    clearInterval(timeInterval);
    stopWatchReset();
})


