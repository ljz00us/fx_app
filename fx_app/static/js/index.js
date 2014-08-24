/**
 * Created by gregorylevin on 7/26/14.
 */


$(document).ready(function () {
    $('#submit').click(function(){
       if($('#query').val().length == 0 ){
          document.getElementById('warning').style.display='block';
          return false;
       }
    });
});