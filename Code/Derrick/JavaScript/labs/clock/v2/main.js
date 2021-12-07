// elements //
const $milliseconds = document.querySelector("#milli");
const $seconds = document.querySelector("#sec");
const $minutes = document.querySelector("#min");
const $hours = document.querySelector("#hours");
const $startBtn = document.querySelector("#start-btn");
const $stopBtn = document.querySelector("#stop-btn");
const $lapBtn = document.querySelector("#lap-btn");
const $resetBtn = document.querySelector("#reset-btn");
const $laps = document.querySelector(".laps");

// vars //
let time;
let milliseconds = `00`;
let seconds = `00`;
let minutes = `00`;
let hours = `00`;
let start;

// set default text to 00:00:00:00 //
$milliseconds.textContent = milliseconds;
$seconds.textContent = seconds;
$minutes.textContent = minutes;
$hours.textContent = hours;

// functions //

// starts watch and formats clock
function startWatch() {
  time = setInterval(() => {
    // new date to calculate difference in milliseconds
    let end = new Date();

    // Format milliseconds to 10s place
    milliseconds = Math.floor(Math.round(end - start)).toString();
    milliseconds = parseInt(milliseconds.slice(-3, -1));

    // format seconds to 10s place and below 60 using milliseconds
    seconds = Math.floor((end - start) / 1000) % 60;

    // format minutes to 10s place and below 60 using milliseconds
    minutes = Math.floor((end - start) / 60000) % 60;

    // format hours to 10s place and below 60 using milliseconds
    hours = Math.floor((end - start) / 3.6e6) % 60;

    // Put a zero in front if not above 10 for visual
    if (seconds % 10 === seconds) {
      seconds = `0${seconds}`;
    }

    if (minutes % 10 === minutes) {
      minutes = `0${minutes}`;
    }

    if (hours % 10 === hours) {
      hours = `0${hours}`;
    }

    // set content for each time span
    $milliseconds.textContent = milliseconds;
    $seconds.textContent = seconds;
    $minutes.textContent = minutes;
  }, 10);
}

// stops watch
function stopWatch() {
  clearInterval(time);
}

// reset watch and clear $laps div of previous laps
function resetWatch() {
  stopWatch();
  let laps = document.querySelectorAll("p");
  laps.forEach((lap) => {
    lap.parentNode.removeChild(lap);
  });
  start = new Date();
  milliseconds = 0;
  seconds = 0;
  minutes = 0;
  hours = 0;
  $milliseconds.textContent = `00`;
  $seconds.textContent = `00`;
  $minutes.textContent = `00`;
}

// prints lap to page
let i = 0;

function printTime() {
  let p = document.createElement("p");
  i++;
  p.innerHTML = `<strong>Lap ${i}</strong> ${hours}:${minutes}:${seconds}:${milliseconds}`;
  $laps.append(p);
}

// event listeners //
$startBtn.addEventListener("click", () => {
  resetWatch();
  i = 0;
  start = new Date();
  startWatch();
});

$stopBtn.addEventListener("click", stopWatch);

$resetBtn.addEventListener("click", resetWatch);

$lapBtn.addEventListener("click", printTime);
