window.onload = function(){
	var signin = document.getElementById('signin');
	var signup = document.getElementById('signup');
	signin.addEventListener("click", funchangein)
	signup.addEventListener("click", funchangeup)

}

function funchangein () {
	 // body...  
	var signin = document.getElementById('signin');
	var signup = document.getElementById('signup');
	var slideBar = document.getElementById("sliderbar");
	var signinform = document.getElementById("view-signin");
	var signupform = document.getElementById("view-signup");
	signup.setAttribute("class", "");
	signin.setAttribute("class", "active");
	slideBar.style.left = '72px';
	signinform.style.display = "block";
	signupform.style.display = "none";
}

function funchangeup () {
	 // body...  
	var signin = document.getElementById('signin');
	var signup = document.getElementById('signup');
	var slideBar = document.getElementById("sliderbar");
	var signinform = document.getElementById("view-signin");
	var signupform = document.getElementById("view-signup");
	signin.setAttribute("class", "");
	signup.setAttribute("class", "active");
	slideBar.style.left = '0px';
	signinform.style.display = "none";
	signupform.style.display = "block";
	 
}