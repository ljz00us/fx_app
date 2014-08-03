/**
 * Created by gregorylevin on 7/26/14.
 */

$(document).ready(function () {

    $('#submit').submit(function(){
       if($('#query').val() == ''){
           alert("Please enter text.");
           return true;
       }
    });
});