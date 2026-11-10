const startPomodoro = document.getElementById("start");
startPomodoro.addEventListener("click", startPomo);
const resetPomodoro = document.getElementById("reset");
resetPomodoro.addEventListener("click", resetPomo);


let timeLeft = 1500;
let isRunning = false;
let interval = null

function updatePomo(){
    const timer = document.getElementById("timer")
    let timeMinutes = Math.floor(timeLeft / 60)
    let timeSeconds = Math.floor(timeLeft % 60)
    let formatedMinutes = String(timeMinutes).padStart(2 , "0")
    let formatedSeconds = String(timeSeconds).padStart(2, "0")

    timer.innerText = `${formatedMinutes}:${formatedSeconds}`;

    
}
function startPomo() {
    if (interval){
        return;
    }
    if (timeLeft > 0) {
        interval = setInterval(()=>{
            timeLeft--
            updatePomo()
        }, 1000)
    }else{
        resetPomo()
    }
}

function resetPomo(){
    clearInterval(interval)
    timeLeft = 1500
    updatePomo()
    interval = null
}