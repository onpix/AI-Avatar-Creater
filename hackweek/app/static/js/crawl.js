$(function(){
    // $('#option2-1').attr('checked','checked');
    // $('#opt2-label1').removeClass('btn-default')
    // .addClass('on');
    // $('input:radio[name="options-2"]').on('change',function(){
    //     $(this).parent().removeClass('btn-default')
    //         .addClass('on').siblings().removeClass('on')
    //         .addClass('btn-default');
    // })
    // $('#option3-1').attr('checked','checked');
    // $('#opt3-label1').removeClass('btn-default')
    // .addClass('on');
    // $('input:radio[name="options-3"]').on('change',function(){
    //     $(this).parent().removeClass('btn-default')
    //         .addClass('on').siblings().removeClass('on')
    //         .addClass('btn-default');
    // });
    $('#option-3').attr("checked",'checked');
    $('#btn-label-3').removeClass('btn-default').addClass('btn-primary');
    $('#option-1').on('change',function(){
        $("#styleimg").attr("src","/static/pic/mode2.png");
        $('#btn-label-1').removeClass('btn-default').addClass('btn-primary').siblings()
        .removeClass('btn-primary')
        .addClass('btn-default');
    });
    $('#option-2').on('change',function(){
        $("#styleimg").attr("src","/static/pic/mode3.png");
        $('#btn-label-2').removeClass('btn-default').addClass('btn-primary').siblings()
        .removeClass('btn-primary')
        .addClass('btn-default');

    }).removeClass('btn-default').addClass('btn-primary');
    $('#option-3').on('change',function(){
        $("#styleimg").attr("src","/static/pic/mode4.png");
        $('#btn-label-3').removeClass('btn-default').addClass('btn-primary').siblings()
        .removeClass('btn-primary')
        .addClass('btn-default');
    }).removeClass('btn-default').addClass('btn-primary');
    $('#option-4').on('change',function(){
        $("#styleimg").attr("src","/static/pic/mode6.png");
        $('#btn-label-4').removeClass('btn-default').addClass('btn-primary').siblings()
        .removeClass('btn-primary')
        .addClass('btn-default');
    }).removeClass('btn-default').addClass('btn-primary');
    $('input:radio[name="options"]').on('change',function(){
        var i ;
        var models=$('#Models');
        models.html('')
        for(i=1;i<=( $('input:radio[name="options"]:checked').val());i++){
            models.append('<option value="'+i+'">'+i+'</option>');
        }
    });
    var img_box_2 = $('#img-box');
    var download = $('#download');
    var crawl_download = $('#crawl-download');
    var crawl_main = $('#crawl-main');
    crawl_download.css('display','none');
    $('#sub-Btn').on("click",function (){
        var form={};
        form['situation'] = $('input:radio[name="options"]:checked').val()
        form['models'] = $('select[name="select-1"] option:selected').val();
        form['level'] = $('select[name="select-2"] option:selected').val();
        form['number'] = $('select[name="select-3"] option:selected').val();
        console.log(form);
        $.ajax({
            url:"/crawl/",
            type:"POST",
            data: form,
            datatype:'json',
            success:function(data){
                crawl_download.css('display','block');
                crawl_main.css('display','none');
                img_box_2.html('<img src="'+data+'" class="img-responsive">');
                download.html('<a href="'+data+'" download="out"><button class="btn btn-primary">下载图片</button></a>');
            },
            error:function(){
                $('mainimg').attr('src','/static/pic/comic.jpg');
            }
        })
    }); 
}
);
