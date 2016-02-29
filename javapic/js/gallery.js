
// function displayUsername() {
// 	var userName = document.getElementsByTagName("span");

// 	userName[0].textContent = "Hello";
	
// };


// //document.createTextNode("Hello, World!");
// var userName = document.getElementsByTagName("span");

// userName.addEventListener('load',displayUsername);

// console.log(displayUsername);

// var x = document.getElementById("myText").value;


window.onload = displayImages;

function displayImages () {

	var getImages = document.getElementById("gallery");

	var tousLesImages = "<ul>";

	for (i = 1; i <= 60; i++) {
		if (i < 10) {
			i = "0" + i;
		}

	var image="<li><img src=images/pdxcg_" + i + ".jpg></li>";

	console.log(displayImages);
	tousLesImages = tousLesImages + image;

}
	tousLesImages = tousLesImages + "</ul>";

	getImages.innerHTML = tousLesImages;
}

function lightBox (event) {
	document.getElementById("image_show").className = "display_img";
	// add event object, make sure you catch it in this function!
	console.log(event.target.src);
	document.getElementById("image_show").firstChild.src=event.target.src;
	
}

document.getElementById("gallery").addEventListener("click", lightBox);

console.log(lightBox);

// third function to get rid of lightbox

