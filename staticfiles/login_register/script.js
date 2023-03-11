$(document).ready(function () {

  // siddhiraj
  var all_okay = true;
  var api_domain = "http://127.0.0.1:8000/api/v1"

  $("#login_proceed_btn").click(function () {

    var fdata = {
      "email": $("#email").val(),
      "password": $("#password").val()
    }

    if (all_okay) {
      $.ajax({
        url: `${api_domain}/accounts/login`,
        type: "POST",
        data: fdata,  

        success: function (result) {
          console.log("Result :: " + result.authToken.access);

          setTimeout(() => {
            
            localStorage.setItem("userData", null);
            localStorage.setItem("authToken", null);
            localStorage.setItem("isUserLoggedIn", null);
  
            localStorage.setItem("userData", result.data);
            localStorage.setItem("authToken", result.authToken.access);
            localStorage.setItem("isUserLoggedIn", true);
          
            window.location = "/";

          }, 3000)



        }
      });
    }

  });


  $("#proceed").click(function () {

    var fdata = {
      "email": $("#email").val(),
      "fname": $("#firstName").val(),
      "lname": $("#lastName").val(),
      "occupation": $("#inputOccupation").val(),
      "gender": $("#gender").val(),
      "phone": $("#mobileNumber").val(),
      "profile_picture": "",
      "password": $("#password").val()
    }

    if (all_okay) {
      $.ajax({
        url: `${api_domain}/accounts/register`,
        type: "POST",
        data: fdata,

        success: function (result) {
          console.log("Result :: " + result);
          window.location = `verify-email/${result.data.action}/${result.data.email}/${result.data.name}`

        }
      });
    }

  });




  // siddhiraj



  $('#emailHelp').hide();
  $('#passwordHelp').hide();
  // Error msg Start
  $('#proceed').click(function () {
    var sEmail = $('#email').val();
    if ($.trim(sEmail).length == 0) {
      $('#emailHelp').show();
      e.preventDefault();
    }
    if (validateEmail(sEmail)) {
      $('#emailHelp').hide();
    } else {
      $('#emailHelp').show();
      e.preventDefault();
    }
  });

  $('#proceed').click(function (event) {
    preventDefault(event);
    if ($('#pass').val().length === 0) { //if pass field is empty
      $('#passwordHelp').show();
    }
    if ($('#pass').val().length) { //if pass has value
      $('#passwordHelp').hide();
      $('#proceed').click(function () {
        window.location("/OTP/index.html");
      });
    }

  });

  function validateEmail(sEmail) {
    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
    if (filter.test(sEmail)) {
      return true;
    } else {
      return false;
    }
  }
  // Error msg End
  // $('.picture').click(function(){

  // })
  // Prepare the preview for profile picture
  $("#wizard-picture").change(function () {
    readURL(this);
  });
});
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
      $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
    }
    reader.readAsDataURL(input.files[0]);
  }
  input.preventDefault()
}

