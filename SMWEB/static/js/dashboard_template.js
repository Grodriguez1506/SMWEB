'use strict'

const report = document.querySelector('#report');
const labelProject = document.querySelector('.label_project');
const inputProject = document.querySelector('.input_project');
const labelDesde = document.querySelector('.label_desde');
const inputDesde = document.querySelector('.input_desde');
const labelHasta = document.querySelector('.label_hasta');
const inputHasta = document.querySelector('.input_hasta');


report.addEventListener('change', () => {
    
    var report_status = report.value;

    if (report_status === 'por proyecto detallado') {
    
        labelProject.style.display= 'block';
        inputProject.style.display= 'block';
        labelDesde.style.display= 'none';
        inputDesde.style.display= 'none';
        labelHasta.style.display= 'none';
        inputHasta.style.display= 'none';
    } else{
        labelProject.style.display= 'none';
        inputProject.style.display= 'none';
        labelDesde.style.display= 'block';
        inputDesde.style.display= 'block';
        labelHasta.style.display= 'block';
        inputHasta.style.display= 'block';
    };

});

