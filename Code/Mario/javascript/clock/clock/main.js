let currentTime = document.querySelector("#current-time");

setInterval(() => {
  const date = new Date();
  currentTime.innerHTML = date.toLocaleTimeString("it-IT");
});

const startBtn = document.querySelector("#start");
const lapBtn = document.querySelector("#lap");
const stopwatch = document.querySelector("#stopwatch");
const stopBtn = document.querySelector("#stop");
const lapTimes = document.querySelector("#lap-times");

let stopWatchInterval;
const date = new Date();
console.log(startBtn);
startBtn.addEventListener("click", () => {
  date.setHours(0, 0, 0, 0);
  stopWatchInterval ? clearInterval(stopWatchInterval) : 0;

  stopWatchInterval = setInterval(() => {
    date.setSeconds(date.getSeconds() + 1);
    stopwatch.textContent = date.toLocaleTimeString("it-IT");
    console.log(date);
  }, 1000);
});

lapBtn.addEventListener("click", () => {
  if (stopWatchInterval) {
    let li = document.createElement("li");
    li.textContent = date.toLocaleDateString("it-IT");
    lapTimes.append(li);
  }
});

stopBtn.addEventListener("click", () => {
  if (stopWatchInterval) {
    clearInterval(stopWatchInterval);
  }
});

const cdInput = document.querySelector("#cd-input");
const units = document.querySelector("#units");
const cdBtn = document.querySelector("#cd-btn");
let cdTimer = document.querySelector("#cd-timer");
let cdInterval;

function countDownTimer() {
  const cdTime = new Date();
  cdTime.setHours(0, 0, 0, 0);
  if (units.value === "seconds") {
    cdTime.setSeconds(cdInput.value - 1);
  } else if (units.value === "minutes") {
    cdTime.setMinutes(cdInput.value - 1, 59);
  } else {
    cdTime.setHours(cdInput.value - 1, 59, 59);
  }

  cdInput.value = "";

  // cdTimer = cdTime.toLocaleDateString("en-GB");
  if (cdInterval) clearInterval(cdInterval);

  cdInterval = setInterval(() => {
    cdTime.setSeconds(cdTime.getSeconds() - 1);
    t = cdTimer.innerHTML = cdTime.toLocaleTimeString("en-GB");
    console.log((cdTimer.innerHTML = cdTime.toLocaleTimeString("en-GB")));
    console.log(cdTime.getHours());
    console.log(cdTime.getMinutes());
    console.log();
    if (
      cdTime.getHours() === 0 &&
      cdTime.getMinutes() === 0 &&
      cdTime.getSeconds() === 0
    ) {
      clearInterval(cdInterval);
      alert("Times up ");
    }
  }, 1000);
}

cdBtn.addEventListener("click", countDownTimer);

const switchClock = document.querySelector("#switch-clock");
const switchStopwatch = document.querySelector("#switch-stopwatch");
const switchCountdown = document.querySelector("#switch-countdown");
const clockDiv = document.querySelector("#clock");
const stopWatchDiv = document.querySelector("#stopwatch-div");
const countdownDiv = document.querySelector("#countdown");

switchClock.addEventListener("click", function () {
  clockDiv.style.display = "block";
  stopWatchDiv.style.display = "none";
  countdownDiv.style.display = "none";
});

switchStopwatch.addEventListener("click", function () {
  clockDiv.style.display = "none";
  stopWatchDiv.style.display = "block";
  countdownDiv.style.display = "none";
});

switchCountdown.addEventListener("click", function () {
  clockDiv.style.display = "none";
  stopWatchDiv.style.display = "none";
  countdownDiv.style.display = "block";
});
