var options = {
    onKeyPress: function (cpf, ev, el, cnpj) {
        var masks = ['00.000.000/0000-00', '00.000.000/0000-00'];
        $('.cnpj').mask((cpf.length > 14) ? masks[1] : masks[0], cnpj);
    }
}
$('.cnpj').length > 11 ? $('.cnpj').mask('00.000.000/0000-00', options) : $('.cnpj').mask('00.000.000/0000-00#', options);

var options = {
    onKeyPress: function (fone, ev, el, fn) {
        var masks = ['(00)00000-0000'];
        $('.telefone').mask((fone.length > 10) ? masks[1] : masks[0], fn);
    }
}
$('.telefone').length > 11 ? $('.cnpj').mask('(00)00000-0000', options) : $('.telefone').mask('(00)00000-0000#', options);


var options = {
    onKeyPress: function (data, ev, el, dt) {
        var masks = ['01/01/2000'];
        $('.dt_nascimento').mask((data.length > 8) ? masks[1] : masks[0], dt);
    }
}
$('.dt_nascimento').length > 8 ? $('.dt_nascimento').mask('01/01/2000', options) : $('.dt_nascimento').mask('01/01/2000#', options);