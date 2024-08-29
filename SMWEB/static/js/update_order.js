'use strict'

const textarea = document.querySelector('.textarea')
const counter = document.querySelector('.counter')
const finish_button = document.querySelector('.finish_order-hidden')
const current_status = document.querySelector('#status')

if (textarea){
    textarea.addEventListener('input', () => {
        counter.textContent = textarea.value.length + "/135"
    })
}

if (current_status){
    current_status.addEventListener('change', () =>{

        var status = current_status.value;
    
        if (status === 'Finalizado'){
            finish_button.style.transition = '450ms';
            finish_button.classList.replace('finish_order-hidden', 'finish_order');
        } else {
            finish_button.style.transition = '450ms';
            finish_button.classList.replace('finish_order', 'finish_order-hidden');
        }
    })
}
