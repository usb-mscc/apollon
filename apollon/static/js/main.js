function checkForm(id, formDiv) {
    $('input:checkbox').removeAttr('checked');
    $('#'+ formDiv +' input:checked').each(function() {
        $(this).prop('checked', false);
    });
    $('input[name='+id+']').prop('checked', true);
}