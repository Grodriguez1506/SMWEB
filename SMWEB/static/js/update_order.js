'use strict'

const textarea = document.querySelector('.textarea')
const counter = document.querySelector('.counter')
const finish_button = document.querySelector('.finish_order-hidden')
const order_status = document.querySelector('#status')

textarea.addEventListener('input', () => {
    counter.textContent = textarea.value.length + "/135"
})

order_status.addEventListener('change', () =>{

    var status = order_status.value;

    if (status === 'Finalizado'){
        finish_button.style.transition = '450ms';
        finish_button.classList.replace('finish_order-hidden', 'finish_order');
    } else {
        finish_button.style.transition = '450ms';
        finish_button.classList.replace('finish_order', 'finish_order-hidden');
    }
})