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

var products = [];

function addStock() {
	var inputs = document.getElementsByTagName("input");
	var cbs = [];
	var checked = [];
	for (var i = 0; i < inputs.length; i++) {
		if (inputs[i].type == "checkbox") {
			cbs.push(inputs[i]);
			if (inputs[i].checked && inputs[i].id != "in-stock") {
				checked.push(inputs[i]);
			var status = inputs[i].parentNode.nextSibling.nextSibling.nextSibling;
			status.textContent = "Yes";
			status.className = "true";
			console.log("in stock!", status);

			} 
		}


	}

	// NOT ALLOWED TO USE querySelectorAll()

	// Find all the selected things

	// Change the inStock value of the selected things

	// Update the display? (Depends on previous step)
	// Find and create a list of all the checked checkbox nodes
}

function removeStock() {
	// USE querySelectorAll()

	var selected = document.querySelectorAll("td>input.selector[type=checkbox]:checked");

	for (var i = 0; i < selected.length; i++) {
		var status = selected[i].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className = "false";
		console.log("last item", status);
	}
}


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

	var newRow = "<tr><td><input type='checkbox'class ='selector'/> </td><td>" + materialName + "</td><td>"
	 + price + "</td><td class=" + inStock + ">" + instockConfirm + "</td></tr>";

	inventory.innerHTML += newRow;

	// Create a new instance of the Product object with the new Item's info
	var newProd = new Product(materialName, price, inStock);
	console.log(newProd);

	products.push(newProd);
}
/* Constructor for teh Product object */
function Product(prodName, price, inStock) {
	this.prodName = prodName;
	this.price = price;
	this.inStock = inStock;

	this.setStock = function(stock) {
		this.inStock = stock;
	}


}



