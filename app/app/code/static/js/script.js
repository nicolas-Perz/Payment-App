
//Recibo los botones de los formularios
let btn_ingresar = document.getElementById('btn-depositar');
let form_ingresar = document.getElementById('form-depositar');
let btn_login = document.getElementById('btn-login');
let form_login = document.getElementById('form-login');

//Les agrego eventos para que al cliquearlos aparezcan
btn_ingresar.addEventListener('click', ()=>{
    form_ingresar.classList.toggle('invisible');
})

<<<<<<< HEAD
let btn_registrarse = document.getElementById('btn-registrarse');
let form_registrarse = document.getElementById('form-registrarse');

btn_registrarse.addEventListener('click', ()=>{
    form_registrarse.classList.toggle('invisible');
})

let btn_login = document.getElementById('btn-login');
let form_login = document.getElementById('form-login');

=======
>>>>>>> 3a904b26f4a0b21507fab83171649360c5f25419
btn_login.addEventListener('click', ()=>{
    form_login.classList.toggle('invisible');
})