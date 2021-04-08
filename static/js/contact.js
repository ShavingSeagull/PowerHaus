$(document).ready(function(){
    // Fires the confirmation modal if the hidden variable in the template is True
    if ($('#fire_modal').val().toBool() == "True") {
        $('#messageModal').modal();
    }
});