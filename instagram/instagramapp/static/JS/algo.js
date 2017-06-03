function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#foto').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#exampleInputFile").change(function(){
  console.log("Entre a esta funcion")
    readURL(this);
});
