var i = 1;

function changeImage() {

	
	// start out with click event listener to change image in jumbotron just to another single image, even if you have to hard code it. Then, see if you can add another image/go through all the images 
	var jumboImage = document.getElementById("jumbotron");

	if (i < 10) {
		i = "0" + i;
	}
	else if (i > 60) {
		i = "0" + 1;
	}

	jumboImage.style.backgroundImage = "url('images/pdxcg_"+ i +".jpg')";
	i++;

}

document.getElementById("jumbotron").addEventListener("click", changeImage);



