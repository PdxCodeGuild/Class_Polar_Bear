var ms=0 , s=0, m=0;
var timer;
var stopwatchEl=document.querySelector('.stopwatch');
var lapsContainer=document.querySelector('.laps');

function start() {
    if (!timer) { timer = setInterval(run,10);}
}

function run() {
    stopwatchEl.textContent = getTimer();
    ms++;
    if (ms === 100){
        ms = 0;
        s++;
    }
    if (s === 60){
        s = 0;
        m++;
    }
}

function pause() {
    stopTimer();
}

function stop() {
    stopTimer();
    ms=0;
    s=0;
    m=0;
    stopwatchEl.contentElement = getTimer();
}
function stopTimer() {
     clearInterval(timer);
    timer = false;
}
function getTimer() {
    return (m<10? "0" + m: m) + ":" + (s<10? "0" + s : s)  + ":" + (ms<10? "0" + ms: ms);
}

function restart() {
    stop();
    start();
}
function lap() {
    if (timer) {
        var li = document.createElement("li");
        li.innerText = getTimer();
        lapsContainer.appendChild(li)
    }
}
function resetLaps() {
    lapsContainer.innerHTML = "";
}



// Lecture Demo
const startButton = document.querySelector('#start');
const lapButton = document.querySelector('#lap');
const stopButton = document.querySelector('#stop');
const stopwatchTimerDemo = document.querySelector('#stopwatch-timer');
const lapTimes = document.querySelector('#lap-times');

let stopwatchInterval;

startButton.addEventListener('click', function() {
  const date = new Date();
  date.setHours(0, 0, 0, 0);
  if (stopwatchInterval) {
    clearInterval(stopwatchInterval)
  }
  stopwatchInterval = setInterval(function() {
    date.setSeconds(date.getSeconds() + 1);
    stopwatchTimerDemo.textContent = date.toLocaleTimeString('it');
  }, 1000);
})

lapButton.addEventListener('click', function() {

})





