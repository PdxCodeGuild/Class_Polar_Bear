let laps = [];

const addZero = num => {
    let str = num + '';
    if(str.length === 1) {
        str = `0${str}`;
    }
    return str;
}

const updateLapsList = () => {
    if(!laps.length) {
        document.querySelector('.laps').classList.add('hidden');
        document.querySelector('.laps ul').innerHTML = '';
        return;
    }
    let htmlStr = laps.reduce((acc, lap, index) => {
        let hours = addZero(new Date(lap).getHours());
        let minutes = addZero(new Date(lap).getMinutes());
        let seconds = addZero(new Date(lap).getSeconds());
        return acc + `<li class="list-group-item">Lap ${index+1}: ${hours}:${minutes}:${seconds}</li>`
    }, '<li class="list-group-item active">Laps</li>');
    document.querySelector('.laps').classList.remove('hidden');
    document.querySelector('.laps ul').innerHTML = htmlStr;
}


function updateTime() {
    let currentTime = new Date();
    let str = currentTime.toLocaleString();
    str = str.split(', ')[1];
    document.querySelector('.current-time-info').innerHTML = str;
}

const updateStartedTime = start => {
    let hours = addZero(new Date(start).getHours());
    let minutes = addZero(new Date(start).getMinutes());
    let seconds = addZero(new Date(start).getSeconds());
    document.querySelector('.start-time-info').innerHTML = `${hours}:${minutes}:${seconds}`;
}

const interval = setInterval(() => {
    updateTime();
}, 1000)

document.querySelector('.start-btn').onclick = () => {
    document.querySelector('.lap-btn').classList.remove('hidden');
    document.querySelector('.start-btn').classList.add('hidden');
    document.querySelector('.start-time').classList.remove('hidden');
    let start = new Date().setHours(0,0,0,0);
    const startInterval = setInterval(() => {
        start = new Date(start).setSeconds( new Date(start).getSeconds() + 1 );
        updateStartedTime(start);
    }, 1000);
    document.querySelector('.lap-btn').onclick = () => {
        laps.push(start);
        updateLapsList();
    }
}

