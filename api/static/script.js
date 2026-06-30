const button = document.getElementById("translateBtn");
const input = document.getElementById("userInput");
const chat = document.getElementById("chatBox");




// utility function 

function getDirection(text){
    const rtlRegex=/[\u0600-\u06FF]/;


    return rtlRegex.test(text)? "rtl":"ltr";
}


//Main Function 

async function sendMessage(){






    const text = input.value.trim();

    const userDir=getDirection(text)

    if(text==="") return;

    chat.innerHTML += `
        <div class="user-message" dir="${userDir}">
            ${text}
        </div>
    `;

    input.value = "";


    const loaddingmessage=document.createElement("div")

    loaddingmessage.className="bot-message"

    loaddingmessage.innerHTML="🤖 Translating..."

    chat.appendChild(loaddingmessage)
    
    chat.scrollTop = chat.scrollHeight;
    input.focus()

    const response = await fetch("/translate",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            text:text
        })
    });

    const data = await response.json();

    loaddingmessage.remove()

    const botDir=getDirection(data.translation)
    chat.innerHTML += `
        <div class="bot-message" dir="${botDir}">
            ${data.translation}
        </div>
    `;
}

button.addEventListener("click", sendMessage)

input.addEventListener("keydown",function(event){

    if (event.key==="Enter"){
 
        event.preventDefault()// دیگه تابع رفتار بالا اجرا نمیشه

        sendMessage()

    }
});
