'use strict'

const order_status = document.getElementsByClassName('orders__element-status');
const sliderContainer = document.querySelector('.slider_container');
const sliderWrapper = document.querySelector('.slider_wrapper');
const sliderElements = document.querySelectorAll('.slider_element');
const totalElements = sliderElements.length;
let currentIndex = 0;

for (let i = 0; i < order_status.length; i++) {

    if (order_status[i].textContent == 'Activo') {
        order_status[i].style.color = 'green';
    } else if (order_status[i].textContent  == 'En ejecucion') {
        order_status[i].style.color = 'orange';
    } else {
        order_status[i].style.color = 'red';
    };
}

if (sliderWrapper){
    // Clonar el primer elemento y añadirlo al final
    const firstElementClone = sliderElements[0].cloneNode(true);
    sliderWrapper.appendChild(firstElementClone);

    // Ajustar el ancho del slider_wrapper al tamaño total de los elementos
    sliderWrapper.style.width = `${800 * (totalElements + 1)}px`;

    function rotateSlider() {
        currentIndex++;

        if (currentIndex > totalElements) {
            // Esperar a que termine la transición y luego reiniciar la posición
            sliderWrapper.style.transition = 'none';
            sliderWrapper.style.transform = 'translateX(0)';
            currentIndex = 0;

            // Forzar el navegador a aplicar el estilo inmediatamente
            // para que el salto sea invisible
            void sliderWrapper.offsetWidth;

            // Rehabilitar la transición
            sliderWrapper.style.transition = 'transform 1000ms ease';
        } else {
            sliderWrapper.style.transform = `translateX(-${currentIndex * 800}px)`;
        }
    }

    // Ejecutar el slider cada 5 segundos
    setInterval(rotateSlider, 3000);
}
