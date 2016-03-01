
// function displayUsername() {
// 	var userName = document.getElementsByTagName("span");

// 	userName[0].textContent = "Hello";
	
// };


// //document.createTextNode("Hello, World!");
// var userName = document.getElementsByTagName("span");

// userName.addEventListener('load',displayUsername);

// console.log(displayUsername);

// var x = document.getElementById("myText").value;

document.addEventListener("click", test);

function test (event) {
	console.log(event.target.nodeName);
} 
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


	if (event.target.nodeName === "IMG") {
		document.getElementById("image_show").className = "display_img";
		document.getElementById("image_show").firstChild.src=event.target.src;
	}
	
}

document.getElementById("gallery").addEventListener("click", lightBox);

console.log(lightBox);

// third function to get rid of lightbox
function removeLightBox (event) {

	if (event.target.nodeName != "IMG") {
	document.getElementById("image_show").firstChild.src=event.target.src;

	document.getElementById("image_show").className="display_none";

	}
}

document.getElementById("image_show").addEventListener("click", removeLightBox);

console.log(removeLightBox);


