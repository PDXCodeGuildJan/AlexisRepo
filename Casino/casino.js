// Number of times we're going to loop
var number = 5;


var inputField = document.getElementById("num-loops");
var counter = document.getElementById("counter");


function loopClick() {
	number = inputField.value;
	counter.innerHTML = "";

	for (var i = 0; i < number; i++) {
		// Print something to the browser's console
		counter.innerHTML += "<img src='dice/" + die() + ".png' alt='A die.'/><br/>";

	};
};

function die() {

	// floor means to round down, whereas 
	dieNumber = Math.floor((Math.random() * 6) + 1 );

	return dieNumber;

};




document.getElementById("loop-btn").onclick = loopClick;