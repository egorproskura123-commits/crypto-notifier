const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopBtn");

const status = document.getElementById("status");


startButton.onclick = async () => {

    const data = {
        code: document.getElementById("code").value,
        coin: document.getElementById("coin").value,
        interval: document.getElementById("interval").value
    };


    const response = await fetch("/start", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(data)
    });


    const result = await response.json();


    if(result.status === "ok"){

        status.innerHTML = "✅ Подписка запущена";

    }else{

        status.innerHTML = "❌ Код не найден";

    }

};



stopButton.onclick = async () => {


    const data = {

        code: document.getElementById("code").value

    };


    const response = await fetch("/stop", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(data)

    });


    const result = await response.json();


    if(result.status === "ok"){

        status.innerHTML = "🛑 Уведомления остановлены";

    }else{

        status.innerHTML = "❌ Код не найден";

    }


};