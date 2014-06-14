
function trim(s)
{
  return s.replace(/^\s+|\s+$/, '');
} 

function validateUsername(fld) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores
 
    if (fld.value == "") {
        fld.style.background = 'Yellow'; 
        error = "You didn't enter a username.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        fld.style.background = 'Yellow'; 
        error = "The username must between 5 and 14 characters.\n";
    } else if (illegalChars.test(fld.value)) {
        fld.style.background = 'Yellow'; 
        error = "The username contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    } 
    return error;
}
/*else if (!((fld.value.search(/(a-z)+/)) && (fld.value.search(/(0-9)+/)))) {
        error = "The password must contain at least one numeral.\n";
        fld.style.background = 'Yellow';
    }*/

function validatePassword(fld,fld2) {
    var error = "";
    var illegalChars = /[\W_]/; // allow only letters and numbers 
 
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "You didn't enter a password.\n";
    } else if ((fld.value.length < 5) || (fld.value.length > 15)) {
        error = "Password must between 5 and 14 characters. \n";
        fld.style.background = 'Yellow';
    } else if (illegalChars.test(fld.value)) {
        error = "The password contains illegal characters.\n";
        fld.style.background = 'Yellow';
    } else if (fld.value != fld2.value) {
        error = "The passwords must be same.\n";
        fld.style.background = 'Yellow';
        fld2.style.background = 'Yellow';
    } else {
        fld.style.background = 'White';
    }
   return error;
}  

function validateEmail(fld) {
    var error="";
    var tfld = trim(fld.value);                        // value of field with whitespace trimmed off
    var emailFilter = /^[^@]+@[^@.]+\.[^@]*\w\w$/ ;
    var illegalChars= /[\(\)\<\>\,\;\:\\\"\[\]]/ ;
    
    if (fld.value == "") {
        fld.style.background = 'Yellow';
        error = "You didn't enter an email address.\n";
    } else if (!emailFilter.test(tfld)) {              //test email for illegal characters
        fld.style.background = 'Yellow';
        error = "Please enter a valid email address.\n";
    } else if (fld.value.match(illegalChars)) {
        fld.style.background = 'Yellow';
        error = "The email address contains illegal characters.\n";
    } else {
        fld.style.background = 'White';
    }
    return error;
}


var allowSubmit = true;
function validateFormOnSubmit(theForm) {
    //prevent multiple submit by restricting submit per 5seconds
    if (!allowSubmit){
        alert('Please press submit after 4 seconds.')
        return false;
    }
    allowSubmit = false;
    setTimeout(function(){ allowSubmit = true; }, 5000);
    //end

    var reason = "";
    reason += validateUsername(theForm.username);      
    reason += validateEmail(theForm.email); 
    reason += validatePassword(theForm.password1,theForm.password2); 
    if (reason != "") {
        alert("Some fields need correction:\n" + reason);
        return false;
    }
    return true;
}