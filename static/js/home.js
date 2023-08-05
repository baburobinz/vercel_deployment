let add_icon = document.getElementById('add_icon');

let icon_wrapper = document.getElementById('icon_wrapper');

let to_do_form = document.getElementsByClassName('add_todo_form');

icon_wrapper.addEventListener('click',function(){

    if (to_do_form[0].style.display=='flex'){

        to_do_form[0].style.display='none';
        add_icon.style.animation='rotate_icon_back 0.2s both ease';
        icon_wrapper.setAttribute('style','background:black;color:white;');

       
    }

    else{

        to_do_form[0].style.display='flex';

        add_icon.style.animation='rotate_icon 0.2s both ease';
        icon_wrapper.setAttribute('style','background:red;color:white;');

    }
})



// sending ajax request to submit to do form


$(document).ready(function(){

    $('#to_do_form').submit(function(event){

        

        event.preventDefault();

        form = $(this);

        url = form.attr('action');

        formData = form.serialize();


        $.ajax({


            url:url,

            type:'POST',

            data:formData,

            success: function(response){

                window.location.href='home';
            }


        });

        
    });




    $('.Delete').click(function(){

       id = $(this).val()

      $('.delete_confirm_window').css('display','flex');


    });


    $('.delete_confirm_window').click(function(){

        $.ajax({

            url:'delete_individual/'+id,
            success:function(request){

                console.log('ok')
            }
        });
    });

   

    $('.sub_content_wrapper').on('click','#edit',function(){


        $(this).text('Save');

        $(this).attr('id','save');


        let editElement = $(this).closest('.todo_container');

        editElement.find('.title_descript').attr('contenteditable',true).focus();

        


        $('.sub_content_wrapper').on('click','#save',function(){


            let get_title = editElement.find('.title').text()

            let get_desc = editElement.find('.desc').text()

            var csrftoken =getCookie("csrftoken");

            let save = $(this);

            let id = $(this).val()


            $.ajax({

                url:'edit_each' ,

                data : {

                    title:get_title,

                    desc: get_desc,
                    id:id,
                },

                headers:{

                    "X-CSRFToken":csrftoken,
                },

                type:'POST',

                success: function(request){


                    var msg = request.success;

                    console.log(msg)


                    save.text('Edit');
                    save.attr('id','edit');
                },
                
                error: function(xhr,errmsg,err){

                    console.log(xhr.status+":"+xhr.responseText)
                }

            
            });
        });

        function getCookie(name){

            var cookieValue = null;

            if (document.cookie && document.cookie !==""){

                var cookies = document.cookie.split(";");
                for (var i=0; i < cookies.length; i++){

                    var cookie = jQuery.trim(cookies[i]);

                    if (cookie.substring(0, name.length + 1)=== name + "="){

                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;

                    }
                }
            }

            return cookieValue;
        }




    });



    


});

