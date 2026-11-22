const startPomodoro = document.getElementById("start");
startPomodoro.addEventListener("click", startPomo);
const resetPomodoro = document.getElementById("reset");
resetPomodoro.addEventListener("click", resetPomo);
const progressBar = document.getElementById("progress");


let currentMode = "focus";
let focusSession = 0;

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


    currentMode = mode.id;

    totalTime = duration;
    timeLeft = duration;

    updateProgress();
    updatePomo();
}


async function sendSessions(duration){
    try{

        const response = await fetch("http://127.0.0.1:5000/sessions",  {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            credentials: "include",

            body: JSON.stringify({
                mode: "focus",
                duration: duration
            })
        })

        const data = await response.json()

        if (!response.ok)   {
            throw new Error(data.erro)
        }

        console.log(data.message)
    } catch (error) {
        console.error("Erro ao registrar sessão", error);
        
    }

}

const numSession = document.getElementById("sessions");

function updateSession() {

    if (currentMode == "focus"){
        numSession.textContent = `${parseInt(numSession.textContent) + 1}` 

        focusSession++;
        sendSessions(totalTime);
    
    
        if (focusSession %4 == 0) {
            setMode(long, 900)
        }else{
            setMode(short, 300)
    }

    }else{
        setMode(focusMode, 1500);
    }


}

function updateProgress() {
    const elapsadeSeconds = totalTime - timeLeft;
    const percentage = (elapsadeSeconds / totalTime) * 100;

    progressBar.style.width = `${percentage}%`
}

function resetPomo(){
    clearInterval(interval)
    interval = null;
    timeLeft = totalTime;

    updatePomo();
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
                clearInterval(interval);
                interval = null;
                updateSession();
            }
        }, 1000)
    }else{
        resetPomo();
    }
}
