const startPomodoro = document.getElementById("start");
startPomodoro.addEventListener("click", startPomo);
const resetPomodoro = document.getElementById("reset");
resetPomodoro.addEventListener("click", resetPomo);

(function(){

    const weekDaysList = ["Domingo","Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    const monthsList = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    function updateDate(){
        const date = new Date
        const month = date.getMonth()
        const day = date.getDate()
        const weekDay = date.getDay()
        const todayDate = document.getElementById("day")
        todayDate.innerText = `${weekDaysList[weekDay]}, ${day} de ${monthsList[month]}`
    }
    updateDate()

    const updateDt = setInterval(updateDate,60000)


})()




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
            if (timeLeft == 0){
                resetPomo()
            }
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