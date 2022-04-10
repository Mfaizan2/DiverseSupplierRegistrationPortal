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
        if(inputValue == 'Yes'){
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
        if(inputValue == 'Yes'){
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
        if(inputValue == 'Yes'){
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
        if(inputValue == 'Yes'){
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
        if(inputValue == 'Yes'){
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
        if(inputValue == 'Yes'){
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


//
//
//
// function downloadCSVFile(csv, filename) {
//     var csv_file, download_link;
//
//     csv_file = new Blob([csv], {type: "text/csv"});
//
//     download_link = document.createElement("a");
//
//     download_link.download = filename;
//
//     download_link.href = window.URL.createObjectURL(csv_file);
//
//     download_link.style.display = "none";
//
//     document.body.appendChild(download_link);
//
//     download_link.click();
// }
//
// function htmlToCSV(html, filename) {
//     var data = [];
//     var rows = document.querySelectorAll("table tr");
//
//     for (var i = 0; i < rows.length; i++) {
//     var row = [], cols = rows[i].querySelectorAll("td, th");
//
//     for (var j = 0; j < cols.length; j++) {
//     row.push(cols[j].innerText);
// }
//
//     data.push(row.join(","));
// }
//
//     downloadCSVFile(data.join("\n"), filename);
// }
//
// document.getElementById("download-button").addEventListener("click", function () {
//     var html = document.querySelector("table").outerHTML;
//     htmlToCSV(html, "excel_data.csv");
// });
//
//
// function generate() {
//     var doc = new jsPDF('p', 'pt', 'letter');
//     var htmlstring = '';
//     var tempVarToCheckPageHeight = 0;
//     var pageHeight = 0;
//     pageHeight = doc.internal.pageSize.height;
//     specialElementHandlers = {
//         // element with id of "bypass" - jQuery style selector
//         '#bypassme': function (element, renderer) {
//             // true = "handled elsewhere, bypass text extraction"
//             return true
//         }
//     };
//     margins = {
//         top: 10,
//         bottom: 10,
//         left: 25,
//         right: 25,
//         width: 1000
//     };
//     doc.setLineWidth(1);
//     // doc.text(200, y = y + 30, "TOTAL MARKS OF STUDENTS");
//     doc.autoTable({
//         html: '#AllRecords',
//         startY: 70,
//         theme: 'striped',
//         margins: margins,
//         columnStyles: {
//             0: {
//                 cellWidth: 60,
//             },
//             1: {
//                 cellWidth: 80,
//             },
//             2: {
//                 cellWidth: 80,
//             },
//             3: {
//                 cellWidth: 50,
//             },
//             4: {
//                 cellWidth: 50,
//             },
//             5: {
//                 cellWidth: 80,
//             },
//             6: {
//                 cellWidth: 70,
//             },
//             7: {
//                 cellWidth: 50,
//             },
//             8: {
//                 cellWidth: 50,
//             }
//         },
//         styles: {
//             minCellHeight: 40
//         }
//     })
//     doc.save('All Records.pdf');
// }
//
// function selectElementContents(el) {
//     var body = document.body, range, sel;
//     if (document.createRange && window.getSelection) {
//         range = document.createRange();
//         sel = window.getSelection();
//         sel.removeAllRanges();
//         try {
//             range.selectNodeContents(el);
//             sel.addRange(range);
//         } catch (e) {
//             range.selectNode(el);
//             sel.addRange(range);
//         }
//     } else if (body.createTextRange) {
//         range = body.createTextRange();
//         range.moveToElementText(el);
//         range.select();
//         range.execCommand("Copy");
//     }
// }




$(document).ready(function() {
    $('#AllRecords').DataTable( {
        dom: 'Bfrtip',
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "responsive": true,
        "lengthChange": true,
        "autoWidth": false,
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5',
            'print',
            'colvis'
        ],
        fixedHeader: true,
        scrollX: true
    } );
} );


// Data Table Dropdown Button Click
$(document).ready(function(){
    $('.buttons-colvis').click(function(){
        $('.dataTables_scrollHead').addClass('header-tbl-index');
        $('.dataTables_scrollBody').addClass('body-tbl-index');
        $('.dataTables_paginate').addClass('pagination-tbl-index');
        $('.dataTables_filter').addClass('search-tbl-index');
        $('.dt-button-background').click(function(){
            $('.dataTables_scrollHead').removeClass('header-tbl-index');
            $('.dataTables_scrollBody').removeClass('body-tbl-index');
            $('.dataTables_paginate').removeClass('pagination-tbl-index');
            $('.dataTables_filter').removeClass('search-tbl-index');
        });
    });
});


function UserSignup()
{
    $form=$('#signup_form');
    var datastring = $form.serialize();
    $.ajax({
        type: "POST",
        url: $form.attr('action'),
        dataType: 'html',
        data: datastring,
        success: function(result)
        {

            var test=JSON.parse(result);
            
            if (test.status === 200)
            {
                $('#signupModal').modal('hide');
                $('#loginModal').modal('show');

                $("#messagesDivLogin").addClass("alert-success");
                $("#outputLabelLogin").text(test.data);
            }
            else
            {
                $("#messagesDiv").addClass("alert-danger");
                $("#outputLabel").text(test.data);
            }

            // $("#loginModal").modal();
            



            // $("#search_modal").modal("show");
        }
    });
}


function UserLogin()
{
    $form=$('#login_form');
    var datastring = $form.serialize();
    $.ajax({
        type: "POST",
        url: $form.attr('action'),
        dataType: 'html',
        data: datastring,
        success: function(result)
        {

            var test=JSON.parse(result);

            if (test.status === 200)
            {
                window.location = '/';
            }
            else
            {
                $("#messagesDivLogin").addClass("alert-danger");
                $("#outputLabelLogin").text(test.data);
            }

            // $("#loginModal").modal();




            // $("#search_modal").modal("show");
        }
    });
}

// function SendResponse()
// {
//     $form=$('#sendResponse_form');
//     $("#emailResponse").removeClass("displayNone");
//     $("#messagesDivSendResponse").addClass("alert-primary");
//     $("#outputLabelSendResponse").text("Sending Response to Submitter");
//     var datastring = $form.serialize();
//     $.ajax({
//         type: "POST",
//         url: $form.attr('action'),
//         dataType: 'html',
//         data: datastring,
//         success: function(result)
//         {
//
//             var test=JSON.parse(result);
//             if (test.status === 200)
//             {
//                 $("#messagesDivSendResponse").removeClass("alert-warning");
//                 $("#messagesDivSendResponse").addClass("alert-success");
//                 $("#outputLabelSendResponse").text(test.data);
//             }
//             else
//             {
//                 $("#messagesDivSendResponse").removeClass("alert-warning");
//                 $("#messagesDivSendResponse").addClass("alert-danger");
//                 $("#outputLabelSendResponse").text(test.data);
//             }
//             setTimeout(function() {
//                 // $('#emailResponse').fadeOut('fast');
//                 $("#emailResponse").addClass("displayNone");
//             }, 2000); // <-- time in milliseconds
//
//         }
//     });
// }

$(document).ready(function(){
    $(function(){
        $('#npmValue').change(function(){
            var opt = $(this).val();

            $('#npmValueCategory1Div').removeClass("displayNone");


            $('#npmValueCategory1').html("");

            $('#npmValueCategory2Div').addClass("displayNone");


            $('#npmValueCategory2').html("");

            var select = document.getElementById("npmValueCategory1");

            $('#npmValueCategory1').prepend('<option value="-1" selected="selected" disabled="disabled">Select Subcategory</option>');

            var arr = [];



            if (opt === "Auxiliaries and supplies")
            {
                arr = [ "Energy", "MRO Material and Standard Parts", "Gases, Lubricants, Chemicals", "Offices supplies", "Personal safety equipment", "Facility Management", "Environmental services", "Catering and canteen services" ]
            }
            else if (opt === "IT and Telecommunication")
            {
                arr = [ "IT Software", "IT Hardware"]
            }
            else if (opt === "IT and Telecommunication(cont.)")
            {
                arr = [ "IT Hardware (cont.)", "IT Operations", "Communication", "IT Services"]
            }
            else if (opt === "Production Equipment and Engineering, Buildings and Vehicles")
            {
                arr = [ "Buildings and utilities", "Plant Equipment, machines, related non-standard parts and services"]
            }
            else if (opt === "Production Equipment and Engineering, Buildings and Vehicles (cont.)")
            {
                arr = [ "Plant Equipment, machines, related non-standard parts and services (cont.)","Vehicles","Repair and maintenance of production equipment",
                        "Engineering and manufacturing Services", "Production Tools"]
            }
            else if (opt === "Corporate Services and Related Supplies")
            {
                arr = [ "Consulting", "Advertising/Marketing services", "Legal Services", "HR services",
                        "Financial services", "Business travel", "Trainings and Seminars"]
            }
            else if (opt === "Logistical Services")
            {
                arr = [ "Freight Services", "Freight Services (cont.)", "Warehouse + distribution service", "Packaging and Labeling"]
            }
            else if (opt === "Logistical Services (cont.)")
            {
                $('#npmValueCategory1Div').addClass("displayNone");
            }
            else
            {
                arr = [];
            }

            jQuery.each(arr, function(i, val) {

                select.options[i+1] = new Option(val, val);
            });

        });
    });
});

$(document).ready(function(){
    $(function(){
        $('#npmValueCategory1').change(function(){
            var opt = $(this).val();

            $('#npmValueCategory2Div').removeClass("displayNone");

            $('#npmValueCategory2').html("");


            var select = document.getElementById("npmValueCategory2");
            $('#npmValueCategory2').prepend('<option value="-1" selected="selected" disabled="disabled">Select Subcategory</option>');

            var arr = [];

            if (opt === "Energy")
            {
                arr = [ "Electricity", "Natural Gas", "Fuel Others", "Outsourced Energy", "Water"]
            }
            else if (opt === "MRO Material and Standard Parts")
            {
                arr = [ "Electrical components", "Hydraulic components", "Pneumatic components", "Mechanical components", "Hand tools", "Machine tools", "Electronics and sensors", "Linear technology", "Workshop and laboratory furniture and equipm"]
            }
            else if (opt === "Gases, Lubricants")
            {
                arr = [ "Technical gase", "Oils, grease, lubricants", "Chemicals (Suppl)", "Mechanical components", "Hand tools", "Machine tools", "Electronics and sensors", "Linear technology", "Workshop and laboratory furniture and equipm"]
            }
            else if (opt === "Offices supplies")
            {
                arr = [ "Office furniture and equipment", "Office material", "Books, subscriptions, forms and printed materials"]
            }
            else if (opt === "Personal safety equipment")
            {
                arr = [ "Personal safety and protective equipment, working clothes", "Medicine and medical equipment"]
            }
            else if (opt === "Facility Management")
            {
                arr = [ "Office and building cleaning", "Office and building cleaning", "Building rep./maint.", "Security / Guard services and building security", "Health Care Services", "Integrated FM", "Employee Transport", "Mold cleaning", "Machine rep./maint."]
            }

            else if (opt === "Environmental services")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "Catering and canteen services")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "IT Hardware")
            {
                arr = [ "IT Printers and scanners"]
            }
            else if (opt === "IT Hardware (cont.)")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "IT Operations")
            {
                arr = [ "IT Consulting and programming", "IT Outsourcing", "IT Infrastructur as a Service (IaaS / PaaS)"]
            }
            else if (opt === "Communication")
            {
                arr = [ "Telecommunications and network infrastructure", "Land line fees", "Mobile fees", "Mobile phone devices"]
            }
            else if (opt === "IT Services")
            {
                arr = [ "IT Application & infrastructure services"]
            }
            else if (opt === "Buildings and utilities")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "Plant Equipment, machines, related non-standard parts and services")
            {
                arr = [ "Controls", "Special purpose machines", "Injection mold machines", "Chipping machines", "Grinding Machines", "Surface treatment equipment and machines",
                        "Automated Measurement Equipment for Mechanical Parameters", "Measurement equip. for electrical / magnetic parameters",
                        "Automated Optical Inspection including X-Ray and Vision test","Measuring equipment for test center and special test purpose",
                        "Welding Machines", "Winding Machines", "Bonding Machines", "Production Machines for Electronic Backend Technologies",
                        "Production Machines for Non-Electronic Technologies", "Machines for pick, place and insertion in electronic prod",
                        "Soldering Equipment", "Screen Printers", "Washing and Cleaning Machines for production"]

            }
            else if (opt === "Plant Equipment, machines, related non-standard parts and services (cont.)")
            {
                arr = ["Erosion Machines", "Machines for temperature controls (TCUs)", "Storage Systems for production areas and Accessories",
                        "Conveyor Systems and Accessories", "Automated tire handling and accessories"];
            }
            else if (opt === "Vehicles")
            {
                arr = [ "Forklifts and industrial trucks", "Cars and vehicles",
                        "Repair and maintenance for forklifts and industrial trucks", "Repair and maintenance for cars and vehicles"]
            }
            else if (opt === "Repair and maintenance of production equipment")
            {
                arr = [ "Installation and relocation services of machines", "Machinery repair (electronical Equipment)",
                        "Machinery repair (mechanical Equipment)", "Maintenance of Test-and Measuring Equipment"]
            }
            else if (opt === "Engineering and manufacturing Services")
            {
                arr = [ "Research projects", "Construction of machines", "Outsourcing Manufacturing Services",
                        "Software & Hardware Requirements", "Software & Hardware Architecture", "Software & Hardware Design (incl. CAD)",
                        "Software Coding, Hardware Comp. Specs.", "Software Code Review, Supplier Test Reports", "Software Module Test, Hardware Simulation & Test",
                        "Software + Hardware Integration", "Software & Hardware Verification", "System Integration and Verification", "R&D Process Support & Know How Transfer",
                        "R&D Test/Measurement", "Industrial Engineering", "Advance Development", "Test-Eng. Temporary labour", "Test-Eng. Others", "R&D M&K:Process/Proj./Q…"]
            }
            else if (opt === "Production Tools")
            {
                arr = [ "Assembly tools & fixture", "Fitting tools", "Tool design change", "Interchange Parts and Workpiece Holder", "Injection Molding Tools"]
            }
            else if (opt === "Consulting")
            {
                arr = [ "Strategy Consulting", "Business Environment Consulting", "Business Operations Consulting", "Technology Consulting", "Auditors & Certificates & Inspections"]
            }
            else if (opt === "Advertising/Marketing services")
            {
                arr = [ "Promotional articles", "Media buying", "Advertising agencies", "Events/Fairs/PR (Marketing)", "Sponsoring", "Market research", "Co-op advertising"]
            }
            else if (opt === "Legal Services")
            {
                arr = [ "Patents and product licencies", "Court and layer fees"]
            }
            else if (opt === "HR services")
            {
                arr = [ "Temp Labor - Light Industria", "Temp Labor - Professional Services", "HR Direct Search", "Jobboards",
                        "Employee relocation services", "Sorting and rework services", "Work & Labour based service contracts",
                        "Translations", "Other HR Services"]
            }
            else if (opt === "Business travel" || opt === "Financial services" || opt === "Trainings and Seminars")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "Freight Services")
            {
                arr = [ "Courier, Express + Parcel Service", "Road freight", "Ocean freight"]
            }
            else if (opt === "Freight Services (cont.)")
            {
                arr = [ "Air freight", "Customs service"]
            }
            else if (opt === "Warehouse + distribution service" || opt === "IT Software")
            {
                $('#npmValueCategory2Div').addClass("displayNone");
            }
            else if (opt === "Packaging and Labeling")
            {
                arr = [ "Cardboard, paper, corrugated", "Labels (barcode, tire etc.)", "Packaging supplies, dunnage",
                        "Liners, foils, separators", "Packaging and marking equipment", "Packaging: Wood", "Packaging: Plastic", "Packaging: Metal", "Tray cleaning"]
            }
            else
            {
                arr = [];
            }

            jQuery.each(arr, function(i, val) {

                select.options[i+1] = new Option(val, val);
            });

        });
    });
});



$(document).ready(function(){
    $(function(){
        $('#pmValue').change(function(){
            var opt = $(this).val();

            $('#pmValueCategory1Div').removeClass("displayNone");


            $('#pmValueCategory1').html("");

            $('#pmValueCategory2Div').addClass("displayNone");


            $('#pmValueCategory2').html("");

            var select = document.getElementById("pmValueCategory1");

            $('#pmValueCategory1').prepend('<option value="-1" selected="selected" disabled="disabled">Select Subcategory</option>');

            var arr = [];



            if (opt === "Raw Material")
            {
                arr = [ "Flat Metal", "Bar Metal", "Wire Metal", "Pipe Metal" ]
            }
            else if (opt === "Casting")
            {
                arr = [ "HighPressure Die Casting", "Sand Casting", "Gravity Die Casting","Gray Iron Casting", "LowPressure Die Casting" ]
            }
            else if (opt === "Non Cast Metal Parts")
            {
                arr = [ "Stamping Parts", "Deep Drawn", "Springs", "Tube Stamping Parts", "Surface Treatment", "Turned Parts",
                        "Turned Parts Steel", "Turned Parts Steel Aluminum", "Turned Parts Steel Brass", "Turned Parts (Hard Steel)",
                        "Aluminum Extrusion", "Forgings/Fasteners", "Brake Pads"]
            }
            else if (opt === "Miscelleanous")
            {
                arr = [ "Soldering & Thick Film", "Potting & Adhesives", "Grease, Lubricants, Oil" ]
            }
            else if (opt === "Plastic Parts")
            {
                arr = [ "Resin", "Thermoplastic Decorative", "Functional Plastic Parts", "Functional Plastics", "Decorative Plastic Parts",
                        "Key/Key Fobs", "Cockpit Parts", "Heads Up Display", "Dials/Pointers"]
            }
            else if (opt === "Rubber Parts")
            {
                arr = [ "Rigid Molded Parts", "Extrusion / Hoses", "Connectivity", "Converting Solutions", "Molded Foams", "Sealing Solutions" ]
            }
            else if (opt === "Electronics")
            {
                arr = [ "Passive" ]
            }
            else if (opt === "Electronics (cont.)")
            {
                arr = [ "Passive (cont.)", "Passive", "ASICS", "Sensor Elements", "Sensors - IC", "Memories", "Transistors", "Multimedia Ics", "Microcontrollers", "Production Related Software" ]
            }
            else if (opt === "Electro-mech Parts")
            {
                arr = [ "Motors & Components", "Electro-Mechanical Assmbl - Connectivit", "Printed Circuit Boards", "Plastic Mechanic & Connectors",
                        "Mechatronics", "Drives", "Batteries", "Switches", "Hybrid Vehicle Comp"]
            }
            else
            {
                arr = [];
            }

            jQuery.each(arr, function(i, val) {

                select.options[i+1] = new Option(val, val);
            });

        });
    });
});


// function SendResponseToSomeone()
// {
//     $form=$('#sendResponseToSomeone_form');
//     $("#emailResponseToSomeone").removeClass("displayNone");
//     $("#messagesDivSendResponseToSomeone").addClass("alert-primary");
//     $("#outputLabelSendResponseToSomeone").text("Sending Response to Submitter");
//     var datastring = $form.serialize();
//     $.ajax({
//         type: "POST",
//         url: $form.attr('action'),
//         dataType: 'html',
//         data: datastring,
//         success: function(result)
//         {
//
//             var test=JSON.parse(result);
//             if (test.status === 200)
//             {
//                 $("#messagesDivSendResponseToSomeone").removeClass("alert-warning");
//                 $("#messagesDivSendResponseToSomeone").addClass("alert-success");
//                 $("#outputLabelSendResponseToSomeone").text(test.data);
//             }
//             else
//             {
//                 $("#messagesDivSendResponseToSomeone").removeClass("alert-warning");
//                 $("#messagesDivSendResponseToSomeone").addClass("alert-danger");
//                 $("#outputLabelSendResponseToSomeone").text(test.data);
//             }
//             setTimeout(function() {
//                 // $('#emailResponse').fadeOut('fast');
//                 $("#emailResponseToSomeone").addClass("displayNone");
//             }, 2000); // <-- time in milliseconds
//
//         }
//     });
// }

function GetFeedbacks()
{
    $form=$('#getFeedbacks_form');

    var datastring = $form.serialize();
    $.ajax({
        type: "POST",
        url: $form.attr('action'),
        dataType: 'html',
        data: datastring,
        success: function(result)
        {

            var test=JSON.parse(result);

            // Find a <table> element with id="myTable":
            var table = document.getElementById("feedback_table");

            var body = ''

            if (test.status === 200) {


                $('#AllFeedBacksDiv').removeClass("displayNone");


                for (const key in test.result) {
                    // var row = table.insertRow(key + 1);
                    body = '<tr>'
                    for (const k in test.result[key]) {

                        if (test.result[key][k]) {
                            body = body + '<td>' + test.result[key][k] + '</td>'
                        } else {
                            body = body + '<td>' + '</td>'
                        }
                    }
                    body = body + '</tr>'
                    $('#feedback_table tbody').append(body);
                }
            }

        }
    });
}


$(document).ready(function(){
    $(function(){
        GetFeedbacks();
    });
});


// Add Span Click
var npmSelectCatOne = null;
var npmSelectCatTwo = null;
var npmSelectCatThree = null;
var npmCount = 0;
var clickCount = 1;
var npmArrayHtml = []; // Store data in Array
$(document).ready(function(){
    $('#npm-select-add').click(function(){
        npmSelectCatOne = $("#select2-npmValue-container").text()
        npmSelectCatTwo = $("#select2-npmValueCategory1-container").text()
        npmSelectCatThree = $("#select2-npmValueCategory2-container").text()
        htmlQuery = npmSelectCatOne + ' > ' + npmSelectCatTwo + ' > ' + npmSelectCatThree
        if(!npmArrayHtml.includes(htmlQuery)){
            npmArrayHtml.push(htmlQuery)
            $("#npmListJquery").append('<li class="npmList'+npmCount+'">'+htmlQuery+'<button class="remove-btn-npm-select" data-id="npmList'+npmCount+'">Remove</button></li>');
        }
        $('.remove-btn-npm-select').click(function(){
            // if( clickCount === 1) {
                let dataID = $(this).attr("data-id")
                let numberStr = dataID.substr(7);
                let index = parseInt(numberStr)
                $("."+dataID).remove(); //Removing the specific List
                let clone = []
                for(let i = 0; i < npmArrayHtml.length; i++){
                    if(npmArrayHtml[i] === npmArrayHtml[index]){}
                    else{
                        clone.push(npmArrayHtml[i])
                    }
                }
                npmArrayHtml = clone
                console.log(npmArrayHtml)
                clickCount++;
            // } else {}
        });
//        let index = npmArrayHtml.indexOf(this);
//        npmArrayHtml.splice(index,1);
       console.log(npmArrayHtml)
        clickCount=1;
        npmCount++;
    });
//    for (let i = 0; i < npmArrayHtml.length; i++) {
//        $("#npmListJquery").append('<li class="npmList'+i+'">'+npmArrayHtml[i]+'<a href="#" class="remove-btn-npm-select" data-id="npmList'+i+'">Remove</a></li>');
//    }
});



