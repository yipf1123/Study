window.onload=function(){
    const pw_show_hide = document.querySelector('.pw_show_hide')
    const id = document.querySelector('#id')
    const pw = document.querySelector('#pw')
    const input_id = document.querySelector('input[type=text]')
    const input_pw = document.querySelector('input[type=password]')
    const id_error = document.querySelector('.id_error')
    const pw_error = document.querySelector('.pw_error')
    console.log(pw_show_hide,input_id,id_error,pw_error)

    // 아이디창 클릭시
 
    let inputFocused = false;

    input_email.addEventListener('focus',function(){
        inputFocused = true;
        input_email.style.boxShadow = '0 2px 0 #0074e9'
    })
    
    input_email.addEventListener('blur',function(){
        inputFocused = false;
        input_email.style.boxShadow = 'none';
        if (input_email.value == '') {
            email_error.style.display = 'none';
        } else if (!isValidEmail(input_email.value)) {
            email_error.style.display = 'block';
            input_email.style.boxShadow = '0 2px 0 #e7223d';
        } else {
            email_error.style.display = 'none';
        }
    })
    
    document.addEventListener('click', function(event) {
        if (!input_email.contains(event.target) && !inputFocused) {
            if (input_email.value != '' && !isValidEmail(input_email.value)) {
                email_error.style.display = 'block';
                input_email.style.boxShadow = '0 2px 0 #e7223d';
            }
        }
    })
    
    function isValidEmail(email) {
        const emailRegExp = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
        return emailRegExp.test(email);
    }
    
    

    // 비밀번호창 클릭시
    let FC_pw = true;  
    input_pw.addEventListener('click', function() {
      if (FC_pw) {
       pw.style.boxShadow = '0 2px 0 #0074e9';
       FC_pw = false;
      }
    });
    input_pw.addEventListener('blur', function() {
        pw_error.style.display = 'block';
        pw.style.boxShadow = '0 2px 0 #e7223d';
      });
      




    // 비밀번호 보이기 안보이기
    let i = true
    pw_show_hide.addEventListener('click',function(){
        const pw_Type = input_pw.getAttribute('type');
        if(i==true){
            input_pw.setAttribute('type', 'text');
            pw_show_hide.setAttribute('title', '문자 숨기기');
            pw_show_hide.style.backgroundPosition = " -126px 0"
            i=false
        }else{
            input_pw.setAttribute('type', 'password');
            pw_show_hide.style.backgroundPosition = " -105px 0"
            i=true
        }
    })
} //onload end