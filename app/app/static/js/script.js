let btn_ingresar = document.getElementById('btn-ingresar');
let form_ingresar = document.getElementById('form-ingresar');

btn_ingresar.addEventListener('click', ()=>{
    form_ingresar.classList.toggle('invisible');
})

let btn_login = document.getElementById('btn-login');
let form_login = document.getElementById('form-login');

btn_login.addEventListener('click', ()=>{
    form_login.classList.toggle('invisible');
})