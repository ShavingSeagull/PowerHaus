$(document).ready(function() {
	// Remove the last three featured products on phone screens to prevent the 
	// user having to scroll for a long period to reach the end of the page
	function addRemoveProducts() {
		const FEATUREDPRODUCTS = document.getElementsByClassName('featured-product');

		if ($(window).innerWidth() <= 576) {
			// Only removes products 3-6, leaving three on-screen
			for (let i = 3; i < FEATUREDPRODUCTS.length; i++) {
				FEATUREDPRODUCTS.item(i).classList.add('d-none');
			}
		} else {
			$('.featured-product').removeClass('d-none');
		}
	}

	// Call the function on page load
	addRemoveProducts();

	// A safeguard to keep the correct number of products on-screen if the 
	// user resizes their browser window
	$(window).resize(() => {
		addRemoveProducts();
	});
});