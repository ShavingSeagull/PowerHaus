$(document).ready(function(){
    // Click listener submits the form when the submit button is clicked. 
    // Needed due to the submit button not being inside the quantity form.
    // DOM traversal needed as forms are rendered in a Jinja loop.
    $(".cart-submit-btn").click(function(e) {
        let form = $(this).parent().prev('.quantity-form');
        form.submit();
    });
});