// Establish the event listener for when they click an item
// Add the click event handler to the "add-item"
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

/* Toggles the inStock sttus on the selected rows inside of inventory.
*/

function addStock() {

	// NOT ALLOWED TO USE querySelectorAll()

	// Find all the selected things

	// Change the inStock value of the selected things

	// Update the display? (Depends on previous step)
}

function removeStock() {
	// USE querySelectorAll()
}

/* Add the itme in the text fields to the inventory
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