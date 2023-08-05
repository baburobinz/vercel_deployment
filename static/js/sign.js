


function onChange(){


    let password = document.getElementById('pword');
    let confPassword = document.getElementById('cnfpword');

    let pword1 = password.value;

    let pword2 = confPassword.value;

   if (pword1==pword2){

    confPassword.setCustomValidity('');
   }

   else{
    confPassword.setCustomValidity('Password did not match..!');

   }

   
}




setTimeout(function(){

    message = document.getElementsByClassName('message');

    message[0].style.display='none';
},2000)