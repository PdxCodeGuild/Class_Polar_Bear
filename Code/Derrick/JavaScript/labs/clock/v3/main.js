const $startTime = document.querySelector("#start-time");
const $addTime = document.querySelector("#time");
const $milliseconds = document.querySelector("#milli");
const $seconds = document.querySelector("#sec");
const $minutes = document.querySelector("#min");

$startTime.addEventListener("click", (event) => {
  event.preventDefault();
  let start = new Date();

  let countdown = setInterval(() => {
    let end = new Date();
    let inputInMilliseconds = $addTime.value * 60000;
    let diff = end - start;
    let result = inputInMilliseconds - diff;
    let milliseconds = Math.floor(Math.round(diff)).toString();
    milliseconds = parseInt(milliseconds.slice(-3, -1));
    let seconds = Math.floor(result / 1000) % 60;
    let minutes = Math.floor(result / 60000) % 60;

    if (inputInMilliseconds - diff === 0) {
      alert("hit zero");
    }
    if (seconds < 10) {
      seconds = `0${seconds}`;
    }
    if (minutes < 10) {
      minutes = `0${minutes}`;
    }

    $milliseconds.textContent = milliseconds;
    $seconds.textContent = seconds;
    $minutes.textContent = minutes;

    if ((seconds <= 0) & (minutes <= 0) & (milliseconds <= 0)) {
      milliseconds = 0;
      $milliseconds.textContent = `00`;
      seconds = 0;
      minutes = 0;
      $seconds.textContent = `00`;
      $minutes.textContent = `00`;
      clearInterval(countdown);
      setTimeout(() => {
        alert("You hit 0!");
      }, 200);
    }
  }, 10);
});

// milliseconds = Math.floor(Math.round(end - start)).toString();
// milliseconds = parseInt(milliseconds.slice(-2));
