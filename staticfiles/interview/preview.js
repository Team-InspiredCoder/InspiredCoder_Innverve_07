// Grab elements, create settings, etc.
var video = document.getElementById('video');

$("#start_interview_btn").click(function () {

    var temp = $("#interview_proceed:checked").val();
    console.log("temp :: ", temp)
    if (temp == "checked") {
        window.location = "/interview-screen";
    } else {
        console.log("Please accept terms and conditions !");
        alert("Please accept terms and conditions !");
    }

});



// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}