$(document).ready(function(){
    $('#file').fileinput({
    language:'zh',
    uploaderUrl:'/',
    allowedFileExtensions:['jpg','png','jpeg'],
    maxFileSize:10000,
    maXFileNum:1,
    showCaption:true,
    dropZoneEnabled:true,
    browseClass:"btn btn-primary",
    showPreview:true,
    showUpload:true
    });
    var img_box = $('#img-box');
    var download = $('#download');
    var draw_download = $('#draw-download');
    var draw_main = $('#draw-main');
    draw_download.css('display','none');
    $('#option-3').attr("checked",'checked');
    $('#btn-label-3').removeClass('btn-default').addClass('on');
    $('#option-1').on('change',function(){
        $("#styleimg").attr("src","/static/pic/sumiao.jpeg");
        $('#btn-label-1').removeClass('btn-default').addClass('on').siblings()
        .removeClass('on')
        .addClass('btn-default');
    });
    $('#option-2').on('change',function(){
        $("#styleimg").attr("src","/static/pic/comic.jpg");
        $('#btn-label-2').removeClass('btn-default').addClass('on').siblings()
        .removeClass('on')
        .addClass('btn-default');

    }).removeClass('btn-default').addClass('on');
    $('#option-3').on('change',function(){
        $("#styleimg").attr("src","/static/pic/vango.jpeg");
        $('#btn-label-3').removeClass('btn-default').addClass('on').siblings()
        .removeClass('on')
        .addClass('btn-default');
    }).removeClass('btn-default').addClass('on');
    $('#option-4').on('change',function(){
        $("#styleimg").attr("src","/static/pic/vango.jpeg");
        $('#btn-label-4').removeClass('btn-default').addClass('on').siblings()
        .removeClass('on')
        .addClass('btn-default');
    }).removeClass('btn-default').addClass('on');
    $('#sub-Btn').on('click',function(){
        console.log($('input:radio[name="options"]:checked').val());
        var formData = new FormData();
        console.log($('#file')[0].files[0]);
        formData.append('file',$('#file')[0].files[0])
        formData.append('model',$('input:radio[name="options"]:checked').val());
        formData.append('level',$('select[name="select-1"] option:selected').val());
        formData.append('times',$('select[name="select-2"] option:selected').val());
        console.log(formData);
        $.ajax({
            url:'/draw/',
            type:'POST',
            data:formData,
            cache:false,
            processData:false,  
            contentType:false,
            success:function(data){
                draw_download.css('display','flex');
                draw_main.css('display','none');
                img_box.html('<img src="'+data+'" class="img-responsive">');
                download.html('<a href="'+data+'" download="out"><button class="btn btn-primary">下载图片</button></a>');
            }
        })
    });
 }
 );