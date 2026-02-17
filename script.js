function sendverification()
{
    let email=document.getElementById("email").value;

    fetch("http://127.0.0.1:5000/send-veri",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({email:email})
    })
    .then(res=>res.json())
    .then(data=>{
        window.serverOTP=data.NUM;
        showPopup1("A verification code has been send to your mail");
    })
    .catch(err=>{
        showPopup("Error");
    });
    return false;
}

function verifycode()
{
    const value=document.getElementById("veri-num").value;
    if(value!=window.serverOTP)
    {
        document.getElementById("popup-message2").innerText="Wrong number entered!!";
        return;
    }
    document.getElementById("popup-message2").innerText="Verified sucessfully!!";
    sendToDB();
}



function sendToDB() {
    let email = document.getElementById("email").value;
    let phone = document.getElementById("tel").value;

    fetch("http://127.0.0.1:5000/subscribe", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            phone: phone
        })
    })

    .then(res => res.json())
    .then(data => {
        showPopup("Saved in MySQL ✅");
    })
    .catch(err => {
        console.error(err);
        showPopup("Error saving data ❌");
    }); 
}



function showPopup(message) {
    document.getElementById("popup-message").innerText = message;
    document.getElementById("popup").style.display = "block";
}
function closePopup() {
    document.getElementById("popup").style.display = "none";
}


function showPopup1(message) {
    document.getElementById("popup-message1").innerText = message;
    document.getElementById("popup1").style.display = "block";
}
function closePopup1() {
    document.getElementById("popup1").style.display = "none";
}