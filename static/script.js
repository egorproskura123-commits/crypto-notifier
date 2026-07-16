console.log("JS работает");
const button = document.getElementById("startButton");

button.addEventListener("click", async function () {

    const code = document.getElementById("code").value;

    const coin = document.getElementById("coin").value;

    const interval = document.getElementById("interval").value;

    const response = await fetch("/start", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            code: code,

            coin: coin,

            interval: interval

        })

    });

    const result = await response.json();

    const status = document.getElementById("status");

    if(result.status === "ok"){

        status.innerText = "🟢 Подписка успешно запущена!";

    }

    else{

        status.innerText = "🔴 Код не найден.";

    }

});
document
    .getElementById("stopBtn")
    .onclick = async () => {

    const code =
        document.getElementById("code").value;

    const response = await fetch("/stop", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            code: code
        })
    });

    const data = await response.json();

    if (data.status === "ok")
        alert("Подписка остановлена!");

    else
        alert("Неверный код");
}