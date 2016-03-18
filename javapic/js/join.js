// Function to make sure my javascript document is connected to its equivalent HTML
function externalJava() {

	console.log("Your JS is connected.");
}

externalJava();

// 1. Add form validation that works in all major browsers

// Function that deactivates browser validate
function deactivateBrowserVal() {
	// Create variable that references the signup fields from the HTML
	var signup = document.getElementById("signup");

	// builtin function novalidate and set to true to turn off because default is false
	signup.novalidate = true;
}

window.onLoad = deactivateBrowswerVal();
document.createAttribute("novalidate");