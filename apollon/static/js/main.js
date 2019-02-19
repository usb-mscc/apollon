function checkForm(id, formDiv, state) {
    $('input:checkbox').removeAttr('checked');
    // $('#'+ formDiv +' input:checked').each(function() {
    //     $(this).prop('checked', false);
    // });
    $('input[name='+id+']').prop('checked', state);
}