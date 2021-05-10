$(document).ready(function() {
    // Code inspired by W3Schools:
    // https://www.w3schools.com/howto/howto_js_navbar_sticky.asp

    let nav = document.getElementById("product-nav");
    let sticky = nav.offsetTop;

    function skinnyNav() {
        if (window.pageYOffset >= sticky) {
            nav.classList.add("sticky-nav");
        } else {
            nav.classList.remove("sticky-nav");
        }
    }

    window.onscroll = function() {
        skinnyNav();
    };
});