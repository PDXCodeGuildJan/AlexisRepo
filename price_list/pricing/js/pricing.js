// Establish the event listener for when they click an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

/* Toggles the inStock sttus on the selected rows inside of inventory.
*/

function addStock() {
	var inputs = document.getElementsByTagName("input");
	var cbs = [];
	var checked = [];
	for (var i = 0; i < inputs.length; i++) {
		if (inputs[i].type == "checkbox") {
			cbs.push(inputs[i]);
			if (inputs[i].checked) {
				checked.push(inputs[i]);
				if (inputs[i].id === "in-stock") {
					checked.push(inputs[i]);
				}

			}
		}

	}
	console.log("This is the list for adding stock ", checked);

	// NOT ALLOWED TO USE querySelectorAll()

	// Find all the selected things

	// Change the inStock value of the selected things

	// Update the display? (Depends on previous step)
	// Find and create a list of all the checked checkbox nodes
}

function removeStock() {
	// USE querySelectorAll()

	var inputs = document.querySelectorAll("td>input[type=checkbox]:checked");

	// var inputs = document.querySelectorAll("input");
	// var cbs = [];
	// var checked = [];
	// for (var i = 0; i < inputs.length; i++) {
	// 	if (inputs[i].type == "checkbox") {
	// 		cbs.push(inputs[i]);
	// 		if (inputs[i].checked) {
	// 			checked.push(inputs[i]);
	// 			if (inputs[i].id === "in-stock") {
	// 				checked.push(inputs[i]);
	// 			}

	// 		}
	// 	}
	// }
	console.log("This is the list for removing stock ", inputs);

}

/* Add the item in the text fields to the inventory
* list, which is in the table body (id="inventory")
*/
function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var inStock = document.getElementById("in-stock").checked;

	if (inStock == true) {
		instockConfirm = "Yes";
	}
	else if (inStock == false) {
		instockConfirm = "No";
	}
	var inventory = document.getElementById("inventory");

	var newRow = "<tr><td><input type='checkbox'/> </td><td>" + materialName + "</td><td>"
	 + price + "</td><td class=" + inStock + ">" + instockConfirm + "</td></tr>";

	inventory.innerHTML += newRow;
}