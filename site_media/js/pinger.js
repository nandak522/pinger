function check_status(domain_id){
    $.ajax({
        url:'/check_status/',
        data:{'domain_id':domain_id},
        type:'POST',
        success: function(response){
            if(response == '200')
                color_up('#check_'+domain_id);
            else
                color_down('#check_'+domain_id);
        },
        beforeSend:function(){
            $('#check_'+domain_id).attr('class', 'check_now');
            $('#check_'+domain_id).text('Pinging...');
        },
        error: function(response){
            $('#check_'+domain_id).text('Error. Please Try Again!');
        }
    });
}

function color_up(element_id){
    $(element_id).text('Up');
    $(element_id).attr('class', 'green');
}

function color_down(element_id){
    $(element_id).text('Down');
    $(element_id).attr('class', 'red');
}

function check_all(){
    $('#ping_all').attr('value', 'Pinging...');
    $('#ping_all').attr('disabled', 'disabled');
    $.getJSON('/check_all/','',function(json_response){
        check_nows = $('.check_now');
        for(i=0;i<check_nows.length;i++){
            domain_id = check_nows[i].id.substring(6);
            if(json_response[domain_id] == '200')
                color_up('#check_'+domain_id);
            else
                color_down('#check_'+domain_id)
        }
        $('#ping_all').removeAttr('disabled');
        $('#ping_all').attr('value', 'Ping Again ?');
    });
}