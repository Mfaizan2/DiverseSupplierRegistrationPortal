// $(document).ready(function(){
//     $(".signin-btn").click(function(){
//         $("#signIn").addClass("d-none");
//         $("#signUp").removeClass("d-none");
//     });
//     $(".signup-btn").click(function(){
//         $("#signIn").removeClass("d-none");
//         $("#signUp").addClass("d-none");
//     });
// });


// Animation On Windows Load
// Old Jquery
// $(window).load(function() {
//     alert("window is loaded");
//     // Handler for .load() called.
// });

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()
// Jquery 3.0
$( window ).on("load", function() {
    // Handler for .load() called.
    $(".banner-img-content").addClass("animate-backInRight");
});



// Select2 Jquery
$(document).ready(function() {
    $('.state-select').select2();
});



// MBE on Radio Button Click
$(document).ready(function(){
    $('.nmsdc-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.nmsdcDetail').removeClass('d-none');
        }
        else {
            $('.nmsdcDetail').addClass('d-none');
        }
    });
});
// WBE on Radio Button Click
$(document).ready(function(){
    $('.wbenc-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.wbencDetail').removeClass('d-none');
        }
        else {
            $('.wbencDetail').addClass('d-none');
        }
    });
});
// VOB on Radio Button Click
$(document).ready(function(){
    $('.vob-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.vobDetail').removeClass('d-none');
        }
        else {
            $('.vobDetail').addClass('d-none');
        }
    });
});
// OC on Radio Button Click
$(document).ready(function(){
    $('.oc-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.ocDetail').removeClass('d-none');
        }
        else {
            $('.ocDetail').addClass('d-none');
        }
    });
});
// Detail View Response on Radio Button Click
$(document).ready(function(){
    $('.srs-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'Custom Response'){
            $('.response-custom-msg').removeClass('d-none');
        }
        else {
            $('.response-custom-msg').addClass('d-none');
        }
    });
});
// Detail View Report on Radio Button Click
$(document).ready(function(){
    $('.report-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'Custom Report'){
            $('.report-custom-msg').removeClass('d-none');
        }
        else {
            $('.report-custom-msg').addClass('d-none');
        }
    });
});
// Oem on Radio Button Click
$(document).ready(function(){
    $('.oem-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.oem-supplier-product').removeClass('d-none');
        }
        else {
            $('.oem-supplier-product').addClass('d-none');
        }
    });
});
// Supply on Radio Button Click
$(document).ready(function(){
    $('.supply-radio-click').click(function(){
        var inputValue = $(this).attr("value");
        if(inputValue == 'yes'){
            $('.vendor-number').removeClass('d-none');
        }
        else {
            $('.vendor-number').addClass('d-none');
        }
    });
});







// Chart JS Content Goes Here
const labels = [ 'January', 'February', 'March', 'April', 'May', 'June', ];
const barData = {
    labels: labels,
    datasets: [{
        label: 'Minority Owned Businesses',
        backgroundColor: 'rgb(49 59 84)',
        borderColor: 'rgb(49 59 84)',
        data: [7, 10, 5, 2, 20, 30, 45],
    },
        {
            label: 'Women Owned Businesses',
            backgroundColor: 'rgb(235 93 10)',
            borderColor: 'rgb(235 93 10)',
            data: [7, 10, 15, 20, 30, 46, 25],
        }]
};

const barConfig = {
    type: 'bar',
    data: barData,
    options: {}
};
const diverseCertificateChart = new Chart(
    document.getElementById('diverseCertificateChart'),
    barConfig
);
const applicationStateChart = new Chart(
    document.getElementById('applicationStateChart'),
    barConfig
);

// Doughnut Chart and settings
const doughnutData = {
    labels: [ 'United State', 'Canada', 'Mexico', 'United Kingdom', 'Australia', 'India', 'Russia', 'China', 'Japan' ],
    datasets: [{
        label: 'Counteries',
        data: [300, 50, 100, 70, 40, 90, 40, 20, 10],
        backgroundColor: [ 'rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)', 'rgb(235 93 10)', 'rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)', 'rgb(201, 203, 207)' ],
        hoverOffset: 4
    }]
};
const doughnutConfig = {
    type: 'doughnut',
    data: doughnutData,
};
const perCountryChart = new Chart(
    document.getElementById('perCountryChart'),
    doughnutConfig
);
const pmChart = new Chart(
    document.getElementById('pmChart'),
    doughnutConfig
);
// Location Chart and settings
const doughnutDataLocation = {
    labels: [ 'Global' ],
    datasets: [{
        label: 'Global chart',
        data: [100],
        backgroundColor: [ 'rgb(255, 159, 64)'],
        hoverOffset: 4
    }]
};
const doughnutLocationConfig = {
    type: 'doughnut',
    data: doughnutDataLocation,
};
const perLocationChart = new Chart(
    document.getElementById('perLocationChart'),
    doughnutLocationConfig
);
// Oem Chart and settings
const doughnutDataOem = {
    labels: [ 'Bmw', 'Honda', 'Audi', 'Lamborghini' ],
    datasets: [{
        label: 'Oem chart',
        data: [90, 40, 20, 10],
        backgroundColor: [  'rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)' ],
        hoverOffset: 4
    }]
};
const doughnutOemConfig = {
    type: 'doughnut',
    data: doughnutDataOem,
};
const perOemChart = new Chart(
    document.getElementById('perOemChart'),
    doughnutOemConfig
);
const npmChart = new Chart(
    document.getElementById('npmChart'),
    doughnutOemConfig
);