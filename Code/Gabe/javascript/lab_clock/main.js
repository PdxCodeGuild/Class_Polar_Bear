// Nav
let defaultActive = true;

const clockNav = document.querySelector('#clock-nav');
const stopwatchNav = document.querySelector('#stopwatch-nav');
const countdownNav = document.querySelector('#countdown-nav');
const clockDiv = document.querySelector('#clock-div');
const stopwatchDiv = document.querySelector('#stopwatch-div');
const countdownDiv = document.querySelector('#countdown-div');

if (defaultActive) {
  clockDiv.style.display = 'block';
  stopwatchDiv.style.display = 'none';
  countdownDiv.style.display = 'none';
}

clockNav.addEventListener('click', function () {
  clockDiv.style.display = 'block';
  stopwatchDiv.style.display = 'none';
  countdownDiv.style.display = 'none';
})
stopwatchNav.addEventListener('click', function () {
  clockDiv.style.display = 'none';
  stopwatchDiv.style.display = 'block';
  countdownDiv.style.display = 'none';
  defaultActive = false;
})
countdownNav.addEventListener('click', function () {
  clockDiv.style.display = 'none';
  stopwatchDiv.style.display = 'none';
  countdownDiv.style.display = 'block';
  defaultActive = false;
})

// Clock
function clockTimer() {
  const d = new Date();
  const clock = document.querySelector('#current-time');
  clock.innerHTML = d.toLocaleTimeString('en-US');
//   clock.textContent =
//   d.getHours()
//   .toString()
//   .padStart(2, 0) +
//   ':' +
//   d.getMinutes()
//   .toString().
//   padStart(2, 0) +
//   ':' +
//   d.getSeconds()
//   .toString()
//   .padStart(2, 0);
}

setInterval(() => {
  clockTimer();
}, 1000);



// Stopwatch
const startBtn = document.getElementById('start-button');
const stopBtn = document.getElementById('stop-button');
const lapBtn = document.getElementById('lap-button');
let hours = '00';
let minutes = '00';
let seconds = '00';
let milliseconds = '00';
const initial = document.querySelector('#stop-watch');

function stopwatch() {
  hours = parseInt(hours);
  minutes = parseInt(minutes);
  seconds = parseInt(seconds);
  milliseconds = parseInt(milliseconds);

  milliseconds++;
  if (milliseconds === 60) {
    seconds++;
    milliseconds = 0;
  }
  if (seconds === 60) {
    minutes++;
    seconds = 0;
  }
  if (minutes === 60) {
    hours++;
    minutes = 0;
  }

  if (hours < 10) {
    hours = '0' + hours;
  }
  if (minutes < 10) {
    minutes = '0' + minutes;
  }
  if (seconds < 10) {
    seconds = '0' + seconds;
  }
  if (milliseconds < 10) {
    milliseconds = '0' + milliseconds;
  }

  return hours + ':' + minutes + ':' + seconds + ':' + milliseconds;
}

const container = document.querySelector('#stop-watch-container');
let stopwatchTimer;

lapBtn.addEventListener('click', function() {
  const lapTimer = document.createElement('p');
  lapTimer.setAttribute('id', 'lap-stop-watch');
  lapTimer.textContent = stopwatch();
  container.appendChild(lapTimer);
});

startBtn.addEventListener('click', function() {
  stopwatchTimer = setInterval(() => {
    const timer = stopwatch();
    let lastChild = container.lastElementChild;
    lastChild.innerHTML = timer;
  }, 10);
})

stopBtn.addEventListener('click', function() {
  clearInterval(stopwatchTimer);
})



// Countdown
const countdownInput = document.querySelector('#countdown-input');
const countdownSelection = document.querySelector('#unit-selection');
const countdownBtn = document.querySelector('#countdown-button');
const cdTimer = document.querySelector('#countdown-timer');
let countdownInterval;

function countdownTimer() {
  const cdTime = new Date();
  cdTime.setHours(0, 0, 0, 0);
  if (countdownSelection.value === 'seconds') {
    cdTime.setSeconds(countdownSelection.value - 1)
  } else
  if (countdownSelection.value === 'minutes') {
    cdTime.setMinutes(countdownSelection.value - 1, 59);
  } else {
    cdTime.setHours(countdownSelection.value - 1, 59, 59);
  }
  cdTimer. = cdTime.toLocaleTimeString('en-GB');

  countdownInterval = setInterval(() => {
    cdTime.setSeconds(cdTime.getSeconds() - 1);
    cdTimer.setContent = cdTime.toLocaleTimeString('en-GB');
  }, 1000);
}

countdownBtn.addEventListener('click', function() {
  countdownTimer();
})


/**
  Adding current date
  const date = new Date();
  console.log(date.getHours());
  console.log(date.getMinutes());
  console.log(date.getSeconds());
 */

// Demo by Anthony
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