
//Recibo los botones de los formularios
let btn_ingresar = document.getElementById('btn-depositar');
let form_ingresar = document.getElementById('form-depositar');
let btn_login = document.getElementById('btn-login');
let form_login = document.getElementById('form-login');

//Les agrego eventos para que al cliquearlos aparezcan
btn_ingresar.addEventListener('click', ()=>{
    form_ingresar.classList.toggle('invisible');
})

btn_login.addEventListener('click', ()=>{
    form_login.classList.toggle('invisible');
})