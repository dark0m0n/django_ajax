function process(){
    $('#click').click(function(){
        let btn = $(this);
        $.ajax(btn.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#form').val()
            },
            'success': function(data){
                document.getElementById('cover').innerHTML += data;
            }
        })
    })
}

$(document).ready(function(){
    process();
})