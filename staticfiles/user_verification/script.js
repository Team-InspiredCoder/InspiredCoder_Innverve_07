
// siddhiraj
  
var api_domain = "http://127.0.0.1:8000/api/v1"

$("#proceed").click(function () {


  var otp = getOTP();

  console.log("otp :: " + otp);
  
  if (otp != false) {
  
    console.log("sending ajax request !")
    var fdata = {
      "email": $("#email").val(),
      "otp": otp,
      "action": $("#action").val()
    }
    
    $.ajax({
      url: `${api_domain}/accounts/verify-user/otp`,
      type: "POST",
      data: fdata,

      success: function (result) {
        console.log("Result :: " + result.data);
        
        localStorage.setItem("userData", result.data);
        localStorage.setItem("authToken", result.authToken.access);
        localStorage.setItem("isUserLoggedIn", true);

        window.location = `/email-verified`

      }
    });
  }

});



// siddhiraj


  // OTP

  function alter_box(id){
    var id_num = parseInt(id.split('')[1]);
    var key = event.keyCode || event.charCode;
    if (key === 8 || key === 46) {
          if(id_num != 1){
            var prev = 'o'+(id_num-1).toString();
            console.log(id_num, prev);
            document.getElementById(prev).focus();
          }
      }else{
        var id_num = parseInt(id.split('')[1]);
      if(id_num!=5){
        var next = 'o'+(id_num+1).toString();
        document.getElementById(next).focus();
      }
      }
  }

  function getOTP(){

    console.log("getting otp !")

    var o1=document.getElementById('o1').value;
    var o2=document.getElementById('o2').value;
    var o3=document.getElementById('o3').value;
    var o4=document.getElementById('o4').value;
    var o5=document.getElementById('o5').value;

    var alert_box = document.getElementById('alert_box');
    if(o1!="" && o2!="" && o3!="" && o4!="" && o5!=""){
      var otp = o1+o2+o3+o4+o5;
      alert_box.style.display = 'none';
      // alert(otp);
      return otp;
    }else{
      alert_box.style.display = 'block';
      return false;
    }
  }
