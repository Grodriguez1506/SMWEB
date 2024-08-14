'use strict'

const menu_icon = document.querySelector('.menu_button');
const side_menu = document.querySelector('#menu');
const element_1 = document.querySelector('.menu__element--1');
const element_2 = document.querySelector('.menu__element--2');
const element_3 = document.querySelector('.menu__element--3');
const notify = document.querySelector('.notify');


function show_menu(){
    element_1.style.transition = 'all 500ms';
    element_2.style.transition = 'all 300ms';
    element_3.style.transition = 'all 500ms';
    element_1.style.transform = 'translateY(15px) rotate(45deg)';
    element_2.style.opacity = '0';
    element_3.style.transform = 'translateY(-11px) rotate(313deg)';
    side_menu.style.overflow = 'scroll';
    notify.style.backgroundColor = 'rgb(0, 0, 255)';
}

function hide_menu(){
    element_1.style.transition = 'all 500ms';
    element_2.style.transition = 'all 300ms';
    element_3.style.transition = 'all 500ms';
    element_1.style.transform = 'translateY(0px) rotate(0deg)';
    element_2.style.opacity = '1';
    element_3.style.transform = 'translateY(0px) rotate(0deg)';
    side_menu.style.overflow = 'hidden';
    notify.style.backgroundColor = 'white';
}



menu_icon.addEventListener('click', function (){
    var menu_class = side_menu.classList;
    if (menu_class[0] === 'hidden_menu') {
        side_menu.classList.replace('hidden_menu','expanded_menu');
        show_menu()
    } else {
        side_menu.classList.replace('expanded_menu','hidden_menu');
        hide_menu()
    }
})
