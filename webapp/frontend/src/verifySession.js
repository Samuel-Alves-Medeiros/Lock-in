document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("http://127.0.0.1:5000/api/me", {
        method: "GET",
        credentials: "include"
    })

    if (!response.ok){
        window.location.replace("login.html");
        return;
    }
    document.querySelector("main").hidden = false;
});