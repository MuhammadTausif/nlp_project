// Must change the base_path before starting the Web app.
// Open the index page in Google chrome, and copy the URL except the index.html
// and paste it to the 'base_path'
var base_path = 'file:///D:/Data/Dev/Python/github/chatterbot/again/halogen_UIs/';
var ws = new WebSocket("ws://localhost:8008");
var global_element;

ws.onmessage = function (event) {
    // alert('message arrived');
    var message_received = event.data;
    message_array = message_received.split(",");
    var sender = message_array.shift();
    // alert("message sender: " + sender);
    var message_text = message_array.join();

    if (sender == 'login') {
        // login code
        if (message_text == "Login OK") {
            $(location).attr('href', base_path + 'question.html');
        }
    }
    if (sender == 'singup') {
        // login code
        if (message_text == "Singup OK") {
            $(location).attr('href', base_path + 'index.html');
        } else {
            alert("User email already exit");
        }
    }
    if(sender == 'proceed'){
        alert('proceed me post back');
    }

    $(location).attr('href', base_path + 'process.html');
    localStorage.setItem('answer_text', sender);
    if(sender == 'yes'){
        // alert('yes me back, answer is: ' + message_text );
    }

};

// Sign Up
$("#singup").on("click", function () {
    global_element = 'singup';
});

$("#login").on("click", function () {
    global_element = 'login';
});

$("#proceed").on("click", function () {
    global_element = 'proceed';
    var question_text = $('#question').val();
    if ( question_text == '') {
        alert('Please enter the question.');
    }
    else {
        localStorage.setItem('question_text', question_text);
        $(location).attr('href', base_path + 'action.html');
    }
});

$("#yes").on("click", function () {
    global_element = 'yes';
    // alert(`${global_element} : is clicked`);
    var question = localStorage.getItem('question_text');
    ws.send(question + ',yes');
    // alert('messege sent');
});

$(".open").on("click", function () {
    $(".popup-overlay, .popup-content").addClass("active");
});

$(".open1").on("click", function () {
    $(".popup-overlay, .popup-content").addClass("active");
});
//removes the "active" class to .popup and .popup-content when the "Close" button is clicked
$(".close, .popup-overlay").on("click", function () {
    $(".popup-overlay, .popup-content").removeClass("active");
});

(function ($) {
    "use strict";


    // When the user clicks on div, open the popup


    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit', function () {
        var check = true;

        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }
        // temp line
        if (check) {
            if (global_element == 'login') {
                // alert(`${global_element} : is clicked`);
                var email = $('#email').val();
                var pass = $('#pass').val();
                ws.send(email + ',' + pass + ',login');
                // alert("message sent");
            }
            if (global_element == 'singup') {
                // alert(`${global_element} : is clicked`);
                var email = $('#email').val();
                var pass = $('#pass').val();
                ws.send(email + ',' + pass + ',singup');
                // alert('messege sent');
            }
            if (global_element == 'yes') {
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    $(document).ready(function() {
       $('#question_text2').val(localStorage.getItem('question_text')).css({ 'color': 'red', 'font-size': '150%'});
       $('#answer_text1').val(localStorage.getItem('answer_text')).css({ 'color': 'black', 'font-size': '150%'});
    });

})(jQuery);
