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
  const clock = document.querySelector('#clock');
  clock.innerHTML = d.toLocaleString();
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

countdownBtn.addEventListener('click', function() {
  let countdownInput = countdownInput.value;
  let selectionValue = countdownSelection.value;
  let hours = '00';
  let minutes = '00';
  let seconds = '00';

  hours = parseInt(hours);
  minutes = parseInt(minutes);
  seconds = parseInt(seconds);

  seconds--;
  66

})
