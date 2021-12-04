const $seconds = document.querySelector("#sec");
const $minutes = document.querySelector("#min");
const $hours = document.querySelector("#hours");
const $amPm = document.querySelector("#am-pm");
let date;

setInterval(() => {
  date = new Date();
  let hours = date.getHours();
  let minutes = date.getMinutes();
  let seconds = date.getSeconds();
  if (hours > 12) {
    hours = hours - 12;
    $amPm.textContent = "PM";
  } else {
    $amPm.textContent = "AM";
  }
  if (hours < 10) {
    hours = `0${hours}`;
  }
  if (minutes < 10) {
    minutes = `0${minutes}`;
  }
  if (seconds < 10) {
    seconds = `0${seconds}`;
  }
  $hours.textContent = hours;
  $minutes.textContent = minutes;
  $seconds.textContent = seconds;
}, 1000);
