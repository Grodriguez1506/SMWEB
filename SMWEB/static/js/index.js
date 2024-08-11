'use strict'

const order_status = document.getElementsByClassName('orders__element-status');

for (let i = 0; i < order_status.length; i++) {
    
    console.log(order_status.length)

    if (order_status[i].textContent == 'Activo') {
        order_status[i].style.color = 'green';
    } else if (order_status[i].textContent  == 'En ejecucion') {
        order_status[i].style.color = 'orange';
    } else {
        order_status[i].style.color = 'red';
    };
}
