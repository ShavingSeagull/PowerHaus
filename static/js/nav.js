$(document).ready(function() {
    const NAV = $("#main-nav");
	const NAV_HIDDEN_ELEMS = $("#nav-list").children('li').children('a').children('span');
	const BUTTON = $("#nav-button");
	const OVERLAY = $(".overlay");
	const PRODUCT_MENU = $('#product-menu');
	const PRODUCT_DROPDOWN = $('.product-dropdown');


	function navControl() {
		if ($(window).innerWidth() <= 1300) {
			if (NAV.css('left') < '0') {
				NAV.css('left', '0');
				BUTTON.css('box-shadow', '0 0');
				OVERLAY.removeClass('d-none');
			} else {
				NAV.css('left', '-100%');
				BUTTON.css('box-shadow', '2px 0 3px #000');
				OVERLAY.addClass('d-none');
			}
		} else {
			if (NAV.width() == 80) {
				NAV.css('width', '210px');
				OVERLAY.removeClass('d-none');
			} else {
				NAV.css('width', '80px');
				OVERLAY.addClass('d-none');
			}
		}
	}

	function showElements() {
		// Checks if the mouse is still on the nav when the function fires after
		// the timeout. This prevents overflow occuring from the user mousing in 
		// and out of the nav quickly. Doesn't apply to smaller devices.
		if ($(window).innerWidth() > 1300) {
			if ($('#main-nav:hover').length != 0) {
				NAV_HIDDEN_ELEMS.removeClass('d-none');
				PRODUCT_DROPDOWN.attr('data-toggle', 'collapse');
			}
		} else {
			NAV_HIDDEN_ELEMS.removeClass('d-none');
			PRODUCT_DROPDOWN.attr('data-toggle', 'collapse');
		}
	}

	function hideElements() {
		NAV_HIDDEN_ELEMS.addClass('d-none');
		PRODUCT_MENU.removeClass('show');
		PRODUCT_DROPDOWN.removeAttr('data-toggle');
	}

	// Event handlers for mousing over on larger screens
	$(NAV).mouseenter(() => {
		navControl();
		// Timeout has to fire slightly after the CSS transition property of 0.4s
		setTimeout(showElements, 410);

	});

	$(NAV).mouseleave(() => {
		navControl();
		hideElements();
	});

	// Click handler for nav button on smaller screens
	$("#nav-button").click(() => {
		navControl();
		showElements();
	});

	// Click handler to close the nav if the user clicks outside the nav
	$(OVERLAY).click(() => {
		navControl();
		NAV_HIDDEN_ELEMS.removeClass('d-none');
	})

	// This acts as a reset in case the user changes their browser window size. 
	// Unlikely to be needed much, but a safeguard nonetheless
	$(window).resize(() => {
		if ($(window).innerWidth() <= 1300) {
			NAV.css({'left': '-100%', 'width': '210px'});
		} else {
			NAV.css({'left': '0', 'width': '80px'});
		}
		OVERLAY.addClass('d-none');
		hideElements();
	});
});