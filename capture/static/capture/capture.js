var capimg= new Image();

 function capture() {
    var c = document.getElementById("mycanvas");
    var ctx = c.getContext("2d");
    capimg = document.getElementById("myimg");
    ctx.drawImage(capimg, 0,0,c.width,c.height);
    var data = c.toDataURL('image/jpeg');
    var request = new XMLHttpRequest();
    request.open("POST","http://127.0.0.1:8000/capture");
    request.send(data)
    /** End **/
}


async function verify()
{
    let formData = new FormData();
    let photo = capimg;
    formData.append("photo", photo);

    const ctrl = new AbortController();    // timeout
    setTimeout(() => ctrl.abort(), 5000);

    try {
       let r =capimg;

       console.log('HTTP response code:',r.status);
    } catch(e) {
       console.log('Huston we have problem...:', e);
    }
    /*var ua = window.navigator.userAgent;

				if (ua.indexOf("Chrome") > 0) {
					// save image without file type
					var canvas = document.getElementById("canvas");
					document.location.href = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");

					// save image as png
					var link = document.createElement('a');
    				link.download = "test.png";
    				link.href=capimg;
    				link.click();
				}
				else {
					alert("Please use Chrome");

				}
				/*var dataURL = document.getElementById('mycanvas').toDataURL("image/png");
                document.getElementById('id_hidden_image_field').value = capimg;*/
}
