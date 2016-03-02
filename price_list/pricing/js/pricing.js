// Establish the event listener for when they click an item
// Add the click event handler to the "add-item"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

var delItemButton = document.getElementById("del-item");
delItemButton.onclick = deleteItem;

/* Toggles the inStock sttus on the selected rows inside of inventory.
*/

var products = [];

window.onload = loadData;

function addStock() {
	var selected = getSelectedRowBoxes(); // <-- use this helper function here in order to re-factor code
	
	for (var i = 0; i < selected.length; i++) { // <-- for loop that loops through list of all Selected Row Boxes. i connotes index and increments according to the length of the list of selected items
		
		var status = selected[i].parentNode.nextSibling.nextSibling.nextSibling; // <-- variable to create status state for whatever was selected at the current index. All the parent/sibling specifications just move us over to the proper column where the stock status will say yes or no
		status.textContent = "Yes"; // <-- stock status will say yes once item has been addStocked
		status.className = "true";
		console.log("in stock!", status);

		var prodId = selected[i].parentNode.parentNode.id;
		products[prodId].inStock = true;


	}
// UPdate the Product in the products array that corresponds to the checked checkbox we're updating.
saveData();
}

function removeStock() {
	// USE querySelectorAll()

	var selected = document.querySelectorAll("td>input.selector[type=checkbox]:checked");

	for (var i = 0; i < selected.length; i++) {
		var status = selected[i].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className = "false";
		console.log("last item", status);

		var prodId = selected[i].parentNode.parentNode.id;
		products[prodId].inStock = false;

		selected[i].checked = false;
	}
	saveData();
}



/* Add the item in the text fields to the inventory
* list, which is in the table body (id="inventory")
*/
function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var inStock = document.getElementById("in-stock").checked;

	var newProd = new Product(materialName, price, inStock);
	products.push(newProd);

	displayInventory();
	saveData();

}

/** 
* Delete the selected rows from the inventory.
**/
function deleteItem() {

	// First, determine all the selected rows
	var selected = getSelectedRowBoxes();

	// Delete the Product objects that correspond to those rows from the products array
	// Loop through the array backwards so the indexes don't shift from the delete/splice
	for (var i = selected.length - 1; i >= 0; i--) {
		// Get the id on the row that the checkbox is in
		var prodId = selected[i].parentNode.parentNode.id;

		// Delete the Ojbect first, leaving a gap
		delete products[prodId];
		// Then remove the gap with a splice
		products.splice(prodId, 1);
	
	};

	// Re-render the HTML list, using displayInventory
	displayInventory();
	saveData();
}

/**
* Helper Function to get all the checked checkboxes in the HTML's inventory
* returns: array of selected checkboxes
**/

function getSelectedRowBoxes() {
	var selected = document.querySelectorAll("td>input.selector[type=checkbox]:checked");

	return selected;
}

/**
* Adds all the items in the products array to the HTML.
**/
function displayInventory() {

	var inventory = document.getElementById("inventory");
	inventory.innerHTML = '';

	// Loop through the products array, adding each Product to the inventory table in HTML
	for (var i = 0; i < products.length; i++) {
		// Make a new row for the Product i
		var newRow = document.createElement("TR");
		newRow.id = i;

		// Make  TD for the checkbox
		var checkbox = document.createElement("TD");
		// Make the actual checkbox
		var innerCheckbox = document.createElement("INPUT");
		// Set the input type to checkbox
		innerCheckbox.type = "checkbox";
		innerCheckbox.className = "selector";
		// Add the checkbox into the TD
		checkbox.appendChild(innerCheckbox);

		// Make  a TD for the material name
		var materialName = document.createElement("TD");
		materialName.textContent = products[i].prodName;

		// Make a TD for the price
		var price = document.createElement("TD");
		price.textContent = products[i].price;

		// Make a TD for the stock toggle
		var inStock = document.createElement("TD");
		//Set the TD's text content to either yes or no, based on the product at index i's inStock property.
		inStock.textContent = (function(inStock) {
			if (inStock) {
				return "yes";
			}
			return "no";
		}(products[i].inStock));
		//inStock.className = products[i].inStock; <-- this does same thing as the setAttribute line of code below it, but setAttribute is more secure
		// Set the class name on the TD
		inStock.setAttribute("class", products[i].inStock);

		// Add all the TDs to the TR
		newRow.appendChild(checkbox);
		newRow.appendChild(materialName);
		newRow.appendChild(price);
		newRow.appendChild(inStock);

		// Add the new row to the actual TBODY in the HTML
		inventory.appendChild(newRow);

	};
	saveData();
}

/* Constructor for the Product object */
function Product(prodName, price, inStock) {
	this.prodName = prodName;
	this.price = price;
	this.inStock = inStock;

	this.setStock = function(stock) {
		this.inStock = stock;
	}


}

/**
* Saves current state of the products array
*/ 
function saveData() {
	// Transform the products array into a JSON string
	var productJSON = JSON.stringify(products);
	console.log("TEST")

	// Save that JSON string to local storage
	localStorage.setItem("price_list", productJSON);
}

/** 
* Loads the current state of the products array.
*/
function loadData() {
	// Load the data from local storage
	var productJSON = localStorage.getItem("price_list");
	console.log("loaded data", productJSON);

	// Parse it into  a javascript data type and save to the global array
	products = JSON.parse(productJSON);

	// Double check that products is set to a list if null
	if (!products) {
		products = [];
	}
	console.log(products);

	displayInventory();

}

