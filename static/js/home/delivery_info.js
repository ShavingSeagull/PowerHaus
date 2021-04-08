$(document).ready(function(){
    // Click listener to toggle the country list and change the icon
    $('.country-list-btn').click(() => {
        if ($('.country-list-btn i').hasClass('fa-door-closed')) {
            $('.country-list-btn i').removeClass('fa-door-closed');
            $('.country-list-btn i').addClass('fa-door-open');
        } else {
            $('.country-list-btn i').removeClass('fa-door-open');
            $('.country-list-btn i').addClass('fa-door-closed');
        }
        $('#country-list').slideToggle();
    });
});