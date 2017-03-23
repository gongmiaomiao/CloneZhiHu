window.onload = function(){
	var btn = document.getElementById('ask1');
	var sub = document.getElementById('sub1');
	btn.addEventListener("click",showmask);
	sub.addEventListener("click",hiddemask);

}

function showmask() {
	var mask = document.getElementById('mask');
	mask.style.display = "block";
}

function hiddemask() {
	var mask = document.getElementById('mask');
	mask.style.display = "none";
}