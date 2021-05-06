
 var capimg= new Image();

 function capture() {
    var c = document.getElementById("mycanvas");
    var ctx = c.getContext("2d");
    capimg = document.getElementById("myimg");
    ctx.drawImage(capimg, 0,0,c.width,c.height);
    var data = capimg;
    }

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function verify()
{
				var dataURL = document.getElementById('mycanvas').toDataURL("image/png");
                //document.getElementById('id_hidden_image_field').value = dataURL;
                dataURL = dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
                var csrftoken = $.cookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);}
            }
    });
    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:8000/capture/verify",
        data: JSON.stringify({
       imageData: dataURL }),
        contentType: 'application/json; charset=utf-8',
        //success: function (msg) {
            //alert("Done, Picture Uploaded.");}
    });
    console.log("Done, Picture Uploaded.");
}
