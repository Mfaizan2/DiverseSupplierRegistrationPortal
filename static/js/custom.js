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

var labels = [  ];
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

// alert("faizan");
// make POST ajax call
$.ajax({
    type: 'POST',
    url: '/diverseCertificationData',
    // data: {
    //     // 'folder_id': JSON.stringify(folder_id),
    // },
    success: function (response) {
        var arrayLength = response['email_error'].length;
        for (var i = 0; i < arrayLength; i++) {
            labels[i]= response['email_error'][i];
        }
        // Chart JS Content Goes Here

        const barData = {
            labels: ['Minority-Owned Business', 'Women-Owned Business', 'Veteran-Owned Business', 'Other Certification'],
            datasets: [{
                label: 'Yes',
                backgroundColor: 'rgb(49 59 84)',
                borderColor: 'rgb(49 59 84)',
                data: [response['BusinessAndCertificationYes'], response['WomenOwnedBusinessYes'], response['VeteranOwnedBusinessYes'], response['OtherCertificationYes']],
            },
                {
                    label: 'No',
                    backgroundColor: 'rgb(235 93 10)',
                    borderColor: 'rgb(235 93 10)',
                    data: [response['BusinessAndCertificationNo'], response['WomenOwnedBusinessNo'], response['VeteranOwnedBusinessNo'], response['OtherCertificationNo']],
                },

                {
                    label: 'In Progress',
                    backgroundColor: 'rgb(54, 162, 235)',
                    borderColor: 'rgb(135 93 10)',
                    data: [response['BusinessAndCertificationInProgress'], response['WomenOwnedBusinessInProgress'], response['VeteranOwnedBusinessInProgress'], response['OtherCertificationInProgress']],
                }
            ]
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

        var labelsForApplicationStates = [ 0 ];

        const barDataForApplicationStates = {
            labels: labelsForApplicationStates,
            datasets: [{
                label: 'Applications Received',
                backgroundColor: 'rgb(49 59 84)',
                borderColor: 'rgb(49 59 84)',
                data: [response['ApplicationReceived']],
            },
                {
                    label: 'Response Generated',
                    backgroundColor: 'rgb(235 93 10)',
                    borderColor: 'rgb(235 93 10)',
                    data: [response['ApplicationsResponse']],
                },

                {
                    label: 'Application Emailed',
                    backgroundColor: 'rgb(135 93 10)',
                    borderColor: 'rgb(135 93 10)',
                    data: [response['ApplicationsEmailed']],
                }
            ]
        };

        const barConfigForApplicationStates = {
            type: 'bar',
            data: barDataForApplicationStates,
            options: {}
        };



        const applicationStateChart = new Chart(
            document.getElementById('applicationStateChart'),
            barConfigForApplicationStates
        );

        // Doughnut Chart and settings
        const doughnutDataForRecordPerCountry = {
            labels: response['totalCountriesArray'],
            datasets: [{
                label: 'Counteries',
                data: response['totalCountriesCount'],
                backgroundColor: [ 'rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)'],
                hoverOffset: 4
            }]
        };
        const doughnutConfigForRecordPerCountry = {
            type: 'doughnut',
            data: doughnutDataForRecordPerCountry,
        };
        const perCountryChart = new Chart(
            document.getElementById('perCountryChart'),
            doughnutConfigForRecordPerCountry
        );
        // Location Chart and settings
        const doughnutDataLocation = {
            labels: response['totalNaLocationArray'],
            datasets: [{
                label: 'Global chart',
                data: response['totalNaLocationCount'],
                backgroundColor: [ 'rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)','rgb(49 59 84)'],
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
            labels: response['totalOemsArray'],
            datasets: [{
                label: 'Oem chart',
                data: response['totalOemsArrayCount'],
                backgroundColor: [  'rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)','rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)','rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)','rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)' ],
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

        const NpmData = {
            labels: response['totalNpmValuesArray'],
            datasets: [{
                label: 'Oem chart',
                data: response['totalNpmValuesCount'],
                backgroundColor: [  'rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)','rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(255, 159, 64)' ],
                hoverOffset: 4
            }]
        };
        const NpmConfig = {
            type: 'doughnut',
            data: NpmData,
        };
        const npmChart = new Chart(
            document.getElementById('npmChart'),
            NpmConfig
        );

        const PmData = {
            labels: response['totalPmValuesArray'],
            datasets: [{
                label: 'Oem chart',
                data: response['totalPmValuesCount'],
                backgroundColor: [  'rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(153, 102, 255)','rgb(49 59 84)', 'rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(255, 159, 64)' ],
                hoverOffset: 4
            }]
        };
        const PmConfig = {
            type: 'doughnut',
            data: PmData,
        };

        const pmChart = new Chart(
            document.getElementById('pmChart'),
            PmConfig
        );

    },
    error: function (response) {
        alert("error");
    }
});





