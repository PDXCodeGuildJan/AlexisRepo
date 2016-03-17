// Created variable i to keep track of image number, as to be to go through all the images via changeImage function
var i = 1;

function changeImage() {
// Function that changes the image currently being displayed
	
	// Created variable to represent image and gained image access via its HTML id
	var jumboImage = document.getElementById("jumbotron");
	// If statement to account for the "0" before all numbers less than 10 so that image number/title is accurate and thus actually displays
	if (i < 10) {
		i = "0" + i;
	}
	// Accounts for what happens at the end of the image gallery because there are only 60 images and they are numbered that way, so this basically makes it so it will start back at the beginning once i goes over 60
	else if (i > 60) {
		i = "0" + 1;
	}

	// changes the background image by taking the static string names of the images (what they all have in common) and just changing the number because that is the only different part and then concatinating those, then incrementing i so it goes through all the images
	jumboImage.style.backgroundImage = "url('images/pdxcg_"+ i +".jpg')";
	i++;

}
// I'm keeping this click event listener as a future reference, just in case, but commented it out because it's not necessary obviously with the setInterval
//document.getElementById("jumbotron").addEventListener("click", changeImage);

// Builtin function setInterval that runs the function changeImage to change the jumbotron image every 10 seconds, specified by the number 10,000 because it is done in milliseconds. 1 second = 1000 ms, so we put 10,000 to indicate we want the function to run (the image to change) every 10 seconds
setInterval(changeImage, 10000);

//Yay, we're done!



