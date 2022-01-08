let timeStart = new Date();
let currentHour = timeStart.getHours()
if (currentHour>12) {
    currentHour = currentHour - 12
}
let currentMinutes = timeStart.getMinutes()
let currentSeconds = timeStart.getSeconds()
let currentTime = ((currentHour) + ':' + currentMinutes + ':' + currentSeconds);
let displayClock = document.querySelector('#clock');



setInterval(clock, 1000);

function clock() {
    timeStart = new Date();
    currentHour = timeStart.getHours()
    if (currentHour>12) {
        currentHour = currentHour - 12
    }
    currentMinutes = timeStart.getMinutes()
    currentSeconds = timeStart.getSeconds()

    currentTime = ((currentHour) + ':' + currentMinutes + ':' + currentSeconds);

    displayClock.textContent = currentTime;
    displayClock.classList.add('clock');
}