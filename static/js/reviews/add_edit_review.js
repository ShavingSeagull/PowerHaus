$(document).ready(function(){
    // Assigns or remove the 'checked' attribute from the custom styled 
    // radio buttons on the add_review page. Radio buttons themselves 
    // aren't visible (the labels mimic a button), hence the need to assign 
    // their 'checked' status via JS.
    const RADIO_BTNS = $('.rating-input');

    $('.rating-label').click(function() {
        $(RADIO_BTNS).removeAttr('checked');
        $(this).prev().attr('checked', 'true');
    })
});