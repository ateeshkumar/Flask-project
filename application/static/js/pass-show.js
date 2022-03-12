const pswrdField=document.querySelector(".form input[type='password']"),
toggleBtn=document.querySelector(".form .field i");

toggleBtn.onclick =()=>{
    if(pswrdField.type == "password"){
        pswrdField.type="text";
        toggleBtn.classList.add("activate");
    }
    else{
        pswrdField.type="password";
        toggleBtn.classList.remove("activate");
    }
}