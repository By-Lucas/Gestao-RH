function UtilizouHoraExtra (id) {
    
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    motivo = document.getElementById('id_utilizada').value;
    
    $.ajax({
        type: "POST",
        url: "/horas-extras/utilizou-hora-extra/" + id,
        data:{
            csrfmiddlewaretoken: token,
            motivo_hora_extra: motivo,
        },
        success: function(result){;
            $("#buttom_text").text(result.buttom_text)

            $("#mensagem_alert").text(result.mensagem);
            $(function() {
                if ($('#mensagem_alert').length) {
                    setTimeout(() => {
                        $('#mensagem_alert').hide('slideUp')
                        setTimeout(() => {
                            $('#mensagem_alert').remove()
                        }, 500)
                    }, 3500)
                }
    
            })
        }
    })
}