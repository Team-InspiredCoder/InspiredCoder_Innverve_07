window.onload = function() {
	const pages = document.querySelectorAll(".page").length;
	const progress = document.querySelector("#progress");
	for(let i=0;i<pages;++i) {
		const span = document.createElement("span");
		span.setAttribute("id", `pageID${i+1}`);
		progress.appendChild(span);
	}
	const children = progress.children;

	const indexOfCurrentPage = () => Math.floor(document.documentElement.scrollTop/window.innerHeight);

	const addActive = (function() {
		let currentActive = indexOfCurrentPage();
		children[currentActive].classList.add("active");

		return () => {
			let index = indexOfCurrentPage();
			if(index === currentActive)
				return;
			if(children[currentActive])
				children[currentActive].classList.remove("active");
			children[index].classList.add("active");
			currentActive = index;
		}

	})();
	addActive();
	document.addEventListener("scroll", addActive);
}


var is_logged_in = localStorage.getItem("isUserLoggedIn");

if (is_logged_in) {
	console.log("User logged in !");
	$(".login").css('visibility', 'hidden')
	// $(".login").css("display", none);
}




const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector("nav");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}

// $('document').ready(function(){
// 	$('.l-btn').click(funtion(){
// 		url: "Login and Registration\index.html",
// 		type: "GET",
// 		success: function(data) {
// 			$('body').hide();
// 			$('body').html(data);
// 			console.log("Success")
// 		}
// 	});
// });