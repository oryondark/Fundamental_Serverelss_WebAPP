//Please, you must upload the image size of 64by64 only!
function ajaxFileUpload(w, h){
  var form = $("#upload_test")[0];
  var formData = new FormData(form);
  $.ajax({
    type:"PUT",
    url:"Endpoint",
    data: formData,
    crossDomain: true,
    processData: false,
    contentType: "multipart/form-data",
    async: false,
    success:function(data){
      console.log(data);
    }
  });
}
