// access divs
let clockDiv = document.getElementById('clock-div');
let stopwatchDiv = document.getElementById('stopwatch-div');
let timerDiv = document.getElementById('timer-div');
let clockButton = document.querySelector('#clock-button');
let stopwatchButton = document.querySelector('#stopwatch-button');
let timerButton = document.querySelector('#timer-button');

clockDiv.style.display = 'none';
stopwatchDiv.style.display = 'none';
timerDiv.style.display = 'none';

clockButton.addEventListener('click', function () {
    clockDiv.style.display = 'block';
    stopwatchDiv.style.display = 'none';
    timerDiv.style.display = 'none';    
})

stopwatchButton.addEventListener('click', function () {
    clockDiv.style.display = 'none';
    stopwatchDiv.style.display = 'block';
    timerDiv.style.display = 'none';    
})

timerButton.addEventListener('click', function () {
    clockDiv.style.display = 'none';
    stopwatchDiv.style.display = 'none';
    timerDiv.style.display = 'block';    
})