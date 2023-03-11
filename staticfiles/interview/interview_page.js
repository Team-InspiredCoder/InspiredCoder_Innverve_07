var countdown = 3;

const myInterval = setInterval(myTimer, 1000);

function myTimer() {
    document.getElementById("show_countdown").innerHTML = countdown;
    countdown -= 1;
    if (countdown <= 0) {
        myStop();
    }
}

function myStop() {
    clearInterval(myInterval);
    $(".interview_start_timer").fadeOut();

    // calling speech recognition
    // runSpeechRecognition();
    // uncomment
    // recordScreen();

    setTimeout(startInterview, 5000);

}



var tcount = 0;
const average = list => list.reduce((prev, curr) => prev + curr) / list.length;

videoList = ["/static/im/videos/first_question.mp4", "/static/im/videos/second_question.mp4", "/static/im/videos/third_question.mp4", "/static/im/videos/fourth_question.mp4", "/static/im/videos/fifth_question.mp4", "/static/im/videos/six_question.mp4", "/static/im/videos/seventh_question.mp4", "/static/im/videos/nine_question.mp4", "/static/im/videos/ten_question.mp4"];
var user_answer = "";
var user_confidence = "";
temp_confidence = [];

var question_count = -1;
var current_user_answer = "";

// speech recognition config
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var recognition = new SpeechRecognition();
recognition.continuous = true;
recognition.interimResults = false;


// let vid = document.getElementById("MainVideo");

function startInterview() {
    // playing intro video
    var vid = document.getElementById("MainVideo");
    vid.play();
    runSpeechRecognition();
}


function askNextQuetion() {

    var vid = document.getElementById("MainVideo");
    $("#MainVideo").removeAttr("loop");
    vid.pause();

    var avgc = 0;
    if (temp_confidence.length > 0) {
        avgc = average(temp_confidence);
    }

    user_answer = `${user_answer} *** ${current_user_answer}`;
    user_confidence = `${user_confidence} *** ${avgc}`;
    temp_confidence = [];
    current_user_answer = "";
    question_count = question_count + 1;

    console.log("\nquestion_count :: " + question_count);
    if (question_count >= 7) {
        endInterview();
    }

    // play next question
    // vid.src = videoList[question_count];
    // if (Questions_Counter == 8) {
    //     vid.pause();
    //     // end_call();

    // }
    document.getElementById("MainVideo").src = videoList[question_count];

    vid.play();

    // display expression video
    runSpeechRecognition();
    // showExpresessionVideo();


    console.log("\nuser_answer_list :: " + user_answer);
    console.log("\nuser_confidence_list :: " + user_confidence);

};


var MainVideo = document.getElementById("MainVideo");
MainVideo.addEventListener('ended', showExpresessionVideo, false);

function showExpresessionVideo(e) {

    console.log("showing expression video!");
    var vid = document.getElementById("MainVideo");
    vid.pause();
    document.getElementById("MainVideo").src = "/static/im/videos/Expression_vid.mp4";
    $("#MainVideo").attr("loop");
    vid.play();

    console.log("Video is finished");
    
}


async function runSpeechRecognition() {

    var prev_index = null;

    recognition.onstart = function () {
        console.log("\nRecognition has started !");
    };

    recognition.onend = function () {
        console.log("\nRecognition has ended !");
        recognition.stop();
        tcount = 0;

        askNextQuetion();
        //showExpresessionVideo();
        // recognition.start();
    }


    recognition.onresult = function (event) {

        console.log("\nRecognized speech !");

        var current = event.resultIndex;

        if (current != prev_index) {
            // stopTrigger();
            prev_index = current;

            var transcript = event.results[current][0].transcript;
            var confidence = event.results[current][0].confidence;

            current_user_answer = `${current_user_answer}. ${transcript}`
            temp_confidence.push(confidence);

            console.log("\nResult :: " + JSON.stringify(event.results));
            console.log("\ntranscript :: " + transcript);
        }

    };

    recognition.start();

}


function stopSpeech() {
    recognition.stop();
    askNextQuetion();
    console.log("Moving to next Question");
};



function mic_toggle() {
    console.log("mic toggle function !");
    var btn_status = $("#mic_btn").text();
    console.log("status :: " + btn_status)


    if (btn_status == 'mic') {
        $("#mic_btn").css('background-color', 'red');
        $("#mic_btn").text('mic_off');

    }
    else {

        $("#mic_btn").css('background-color', '#282828');
        $("#mic_btn").text('mic');
    }
}



$("#timer_div").fadeOut(1);
// $("#interview_end_div").fadeOut(1);


function camera_toggle() {

    console.log("camera toggle function !");
    var btn_status = $("#camera_btn").text();
    console.log("status :: " + btn_status)

    if (btn_status == 'videocam') {
        closing_camera()

        //$("#timer_div").fadeIn(1);
        startTimer(20);
        $("#camera_btn").css('background-color', 'red');
        $("#camera_btn").text('videocam_off');
    }
    else {
        recordVideo();
        //Web_Cam_fun();
        $("#camera_btn").text('videocam');
        $("#timer_div").fadeOut(1);
        $("#camera_btn").css('background-color', '#282828');

    }
}


var x;
function startTimer(timer) {
    $("#Timer").css('background-color', 'grey')
    timer_var = timer;
    clearInterval(x)
    $("#Timer").text("")
    $("#Timer").text(timer_var)
    $("#timer_div").fadeIn(1);
    x = setInterval(() => {
        //$("#Timer").text(timer_var)
        document.getElementById("Timer").innerHTML = timer_var
        timer_var = timer_var - 1;
        if (timer_var < 10) {
            $("#Timer").css('background-color', 'red')
        }
        if (timer_var < -1) {
            $("#timer_div").fadeOut(1);

            clearInterval(x)
            recordVideo();
            // Web_Cam_fun();
            $("#camera_btn").css('background-color', '#282828');
            $("#camera_btn").text('videocam');
        }
    }, 1000)


}


function display_caption(display) {
    if (display) {
        console.log("In if of Display caption")
        //Visible Caption Div
        $("#caption_div").css("visibility", 'visible')

    }
    else {

        $("#caption_div").css("visibility", 'hidden')
        //hidden Caption Div
    }

}

function caption_toggle() {
    display = true
    console.log("caption toggle function !");
    var btn_status = $("#caption_btn").text();
    console.log("status :: " + btn_status)


    if (btn_status == 'closed_caption') {
        $("#caption_btn").css('background-color', 'red');
        $("#caption_btn").text('closed_caption_disabled');
        //recognition.stop()//For Debugging

        display_caption(false)

    }
    else {
        display_caption(true)
        $("#caption_btn").css('background-color', '#282828');
        $("#caption_btn").text('closed_caption');
    }
}


function endInterview() {

    recognition.stop()
    closing_camera();
    $("#interview_end_div").css('visibility', 'visible');
    var vid = document.getElementById("MainVideo");
    $("#MainVideo").removeAttr("loop");
    vid.pause();

    var api_domain = "http://127.0.0.1:8000/api/v1"



    var fdata = {
        "user_answer": user_answer,
        "user_confidence": user_confidence,
    }
    console.log("AuthToken",localStorage.getItem('authToken'))
    $.ajax({
        url: `${api_domain}/report/generate-pdf`,
        type: "POST",
        headers:{'Authorization':"Bearer "+localStorage.getItem('authToken')},

        data: fdata,

        success: function (result) {
            console.log("Result :: " + result.data);
        }
    });

}








// *************************** Video *****************************


// let video = document.getElementById("video_element");
let model;
let canvas = document.getElementById("canvas")
let ctx = canvas.getContext("2d")
// let cls_cam;
let shouldStop = false;
function closing_camera() {
    shouldStop = true;
    const video = document.getElementById('web_cam');

    const mediaStream = video.srcObject;
    const tracks = mediaStream.getTracks();

    // Tracks are returned as an array, so if you know you only have one, you can stop it with:
    tracks[0].stop();
    $("#main_popup").fadeOut();
    // Or stop all like so:
    tracks.forEach(track => track.stop())


    // cls_cam.stop();

}





const setupCamera = () => {
    navigator.mediaDevices
        .getUserMedia({
            video: { width: 600, height: 400 },
            audio: false,
        })
        .then((stream) => {
            video.srcObject = stream;
        });
};


const videoElement = document.getElementById('web_cam');
const parts2 = [];

async function recordVideo() {

    const mimeType = 'video/webm';
    shouldStop = false;
    const constraints = {
        video: {
            "width": {
                "min": 640,
                "max": 1024
            },
            "height": {
                "min": 480,
                "max": 768
            }
        }
    };



    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    videoElement.srcObject = stream;
    handleRecord({ stream, mimeType })






    //setTimeout(recordScreen, 1000);
}


async function recordScreen() {
    console.log("In recordScreen function!!");

    const mimeType = 'video/webm';
    shouldStop = false;
    const constraints = {
        video: {
            cursor: 'motion'
        }
    };
    if (!(navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia)) {
        return window.alert('Screen Record not supported!')
    }
    let stream = null;
    console.log("Ask  Screen Permission...")
    const displayStream = await navigator.mediaDevices.getDisplayMedia({ video: { cursor: "motion" }, audio: { 'echoCancellation': true } });
    if (1) {
        const audioContext = new AudioContext();

        const voiceStream = await navigator.mediaDevices.getUserMedia({ audio: { 'echoCancellation': true }, video: false });
        const userAudio = audioContext.createMediaStreamSource(voiceStream);

        const audioDestination = audioContext.createMediaStreamDestination();
        userAudio.connect(audioDestination);

        if (displayStream.getAudioTracks().length > 0) {
            const displayAudio = audioContext.createMediaStreamSource(displayStream);
            displayAudio.connect(audioDestination);
        }

        const tracks = [...displayStream.getVideoTracks(), ...
            audioDestination.stream.getTracks()]
        stream = new MediaStream(tracks);
        handleRecord({ stream, mimeType })
    } else {
        stream = displayStream;
        handleRecord({ stream, mimeType });
    };


    // main_fun()

}

const handleRecord = function ({ stream, mimeType }) {
    // startRecord()
    console.log("In handle Record!!");
    let recordedChunks = [];
    stopped = false;
    const mediaRecorder = new MediaRecorder(stream);
    // cls_cam = mediaRecorder;

    mediaRecorder.ondataavailable = function (e) {
        if (e.data.size > 0) {
            recordedChunks.push(e.data);
        }

        if (shouldStop === true && stopped === false) {
            mediaRecorder.stop();
            stopped = true;
        }
    };

    mediaRecorder.onstop = function () {
        console.log("In On Stop Of screen Sharing!!")
        const blob = new Blob(recordedChunks, {
            type: mimeType
        });
        recordedChunks = []
        const filename = "InterviewVideo"
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = `${filename || 'recording'}.webm`;
        //   stopRecord();
        videoElement.srcObject = null;
    };

    mediaRecorder.start(200);
};


function check_face_probability(face_probability) {
    face_probability = face_probability * 100

    var btn_status = $("#camera_btn").text();
    btn_status = "videocam"
    if (btn_status == "videocam") {

        if (face_probability < 80) {
            console.log("You are not visibile on Camera Please check your face position otherwise your interview will be terminated");
        }
        else if (face_probability < 95) {
            console.log("You are not properly visible either adjust your camera or change your position");
        }
        else {
            console.log("Good Position")
        }
    }
    else {
        console.log("Camera is closed")
    }

}

Web_Cam_fun()
// recordScreen()
function Web_Cam_fun() {

    navigator.mediaDevices.getUserMedia({ audio: true, video: true }).then(stream => {

        videoElement.srcObject = stream;

        MediaRecorder_new = new MediaRecorder(stream);
        MediaRecorder_new.start(1000);
        MediaRecorder_new.ondataavailable = function (e) {
            parts2.push(e.data);
        }


    });
}

const downloadLink = document.getElementById('video_dnld_link');
document.getElementById("video_dnld_link").onclick = function () {
    shouldStop = true;
    closing_camera();
    MediaRecorder_new.stop();
    const blob_new = new Blob(parts2, {
        type: "video/webm"
    })
    const url_new = URL.createObjectURL(blob_new);
    const a_new = document.createElement("a");
    document.body.appendChild(a_new);
    a_new.href = url_new;
    a_new.download = "Video.webm";
    a_new.click();




}

const detectFaces = async () => {

    const prediction = await model.estimateFaces(videoElement, false);

    try {

        face_probability = prediction[0].probability;
        check_face_probability(face_probability)
        console.log(face_probability * 100)

    }
    catch (error) {

        var btn_status = $("#camera_btn").text();
        btn_status = "videocam"
        error_counter = 0
        can_display_popup = false

        if (btn_status == "videocam") {
            if (error.name == "TypeError") {
                var aud = document.getElementById("myAudio");

                if (error_counter >= 3 && can_display_popup) {
                    //alert(error_counter)
                    //$("#myAudio").attr("loop")

                    console.log("Your Video is terminating")

                }
                else {

                    // showFacepopup("Your are not visible at all");
                    console.log("You are not visible t all")
                }
                if (can_display_popup) {
                    error_counter = error_counter + 1
                    console.log("Error_Counter:", error_counter)
                    console.log("can_display_popup val:", can_display_popup)
                }
                console.log(error_counter)
            }
        }
        else {
            console.log("Camera is closed in Catch block")
        }
    }

    ctx.drawImage(videoElement, 0, 0, 600, 400);
    prediction.forEach((pred) => {
        ctx.beginPath();
        ctx.lineWidth = "4";
        ctx.strokeStyle = "blue"
        ctx.rect(
            pred.topLeft[0],
            pred.topLeft[1],
            pred.bottomRight[0] - pred.topLeft[0],
            pred.bottomRight[1] - pred.topLeft[1]

        );
        //ctx.stroke();


    });
};



videoElement.addEventListener("loadeddata", async () => {
    console.log("InloadedData Listener")

    model = await blazeface.load();
    setInterval(detectFaces, 5000)
});





