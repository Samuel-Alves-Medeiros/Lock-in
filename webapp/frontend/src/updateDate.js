(function(){

    const weekDaysList = ["Domingo","Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"];
    const monthsList = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

    function updateDate(){
        const date = new Date;
        const month = date.getMonth();
        const day = date.getDate();
        const weekDay = date.getDay();
        const todayDate = document.getElementById("day");
        todayDate.innerText = `${weekDaysList[weekDay]}, ${day} de ${monthsList[month]}`;
    }
    updateDate();

    const updateDt = setInterval(updateDate,60000);


})();