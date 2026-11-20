const startPomodoro = document.getElementById("start");
startPomodoro.addEventListener("click", startPomo);
const resetPomodoro = document.getElementById("reset");
resetPomodoro.addEventListener("click", resetPomo);
const progressBar = document.getElementById("progress");

let completedSessions = 0;
let sessionsCounting = 0;


let timeLeft = 1500;
let totalTime = 1500;
let interval = null;


function updatePomo(){
    const timer = document.getElementById("timer");
    let timeMinutes = Math.floor(timeLeft / 60);
    let timeSeconds = Math.floor(timeLeft % 60);
    let formatedMinutes = String(timeMinutes).padStart(2 , "0");
    let formatedSeconds = String(timeSeconds).padStart(2, "0");

    timer.innerText = `${formatedMinutes}:${formatedSeconds}`;
}

const focusMode = document.getElementById("focus");
const short = document.getElementById("short");
const long = document.getElementById("long");

function setMode(mode, duration){

    focusMode.classList.remove("active");
    short.classList.remove("active");
    long.classList.remove("active");
    mode.classList.add("active")
    totalTime = duration;
    timeLeft = duration;
    updateProgress();
    updatePomo();
}

function swapTimer() {
    
    if (sessionsCounting == 3 ) {
        setMode(long, 900);
        sessionsCounting = 0;

        
    } else{

        if (sessionsCounting % 2 == 0 ){
                setMode(focusMode, 1500 );
        
        } else if (sessionsCounting % 2 == 1) {
            
            setMode(short, 300);
                  
        }
    }


}

const numSession = document.getElementById("sessions");

function updateSession() {
    numSession.textContent = `${parseInt(numSession.textContent) + 1}` 
    sessionsCounting++;
    completedSessions++;
    swapTimer();
}

function updateProgress() {
    const elapsadeSeconds = totalTime - timeLeft;
    const percentage = (elapsadeSeconds / totalTime) * 100;

    progressBar.style.width = `${percentage}%`
}

function resetPomo(){
    clearInterval(interval)
    timeLeft = 1500;
    totalTime = 1500;
    updatePomo();
    interval = null;
    updateProgress();
}

function startPomo() {
    if (interval){
        return;
    }
    if (timeLeft > 0) {
        interval = setInterval(()=>{
            timeLeft--
            updatePomo();
            updateProgress();
            if (timeLeft == 0){
                resetPomo();
                updateSession();
            }
        }, 1000)
    }else{
        resetPomo();
    }
}

// Enviar sessões

// fetch("http://127.0.0.1:5000/sessions",  {
//     method: "POST",
//     headers:{
//         "Content-Type": "application/json"
//     },
//     body: JSON.stringify({sessions: completedSessions})
// })