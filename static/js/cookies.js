/*
* Cookie code adapted from:
* https://www.peterfessel.com/2018/11/gdpr-adsense-how-to-create-a-cookie-consent-modal-that-defers-ads-from-loading/
*/
function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}

function setCookie(key, value, days) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString() + ';path=/';
}

$(document).ready(function(){
    // Check if GDPR cookie consent has already been given
	if (!getCookie("consentgiven")) {
        $('#gdpr-modal').modal('show');
    }

	// Click listener for GDPR acceptance on Home page
	$('#gdpr-btn').click(() => {
		setCookie("consentgiven", true, 1);
	});
});