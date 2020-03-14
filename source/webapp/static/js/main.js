

function jqueryParseData (response, status) {
    location.reload(true)

    console.log(response);
    console.log(status);
}

function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function addUserLoadIndex(user, file_id) {
    console.log($('#user_add').val());
    console.log(file_id)
    $.ajax({
        url: 'http://localhost:8000/api/v1/files/' + file_id,
        method: 'PATCH',
        contentType: 'application/json',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({user: user, File: file_id}),
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}
$(document).ready(function () {
        console.log($('#user_add').val())

    // createTasksLoadIndex();
    // deleteTasksLoadIndex();
});