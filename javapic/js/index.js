// Gain access to all of the Gallery Images
function accessImages() {

	var jumboImage = document.getElementById("jumbotron");
	// start out with click event listener to change image in jumbotron just to another single image, even if you have to hard code it. Then, see if you can add another image/go through all the images 

	for (i = 1; i <= 60; i++) {
		if (i < 10) {
			i = "0" + i;
		}
		var image = "<img src=images/pdxcg_" + i + ".jpg>";
	}
	jumboImage = "<img src=images/pdxcg_06.jpg>";
	
}

document.addEventListener("click", accessImages);