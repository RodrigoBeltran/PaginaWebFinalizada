$(document).ready(function(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET','https://randomuser.me/api/?results=4',true)
    xmlhttp.send();


    //crear la estructura//
    var card_usuario = document.getElementById('card-deck');


    //crear los elementos
    var card = document.createElement('card-deck');
    var hcard = document.createElement('card-header');
    var bcard = document.createElement('card-body');
    var fcard = document.createElement('card-footer');


    //encabezado
    var encabezado = [ "NOMBRE", "EMAIL", "EDAD", "GENERO"];
    var filaTitulo = document.createElement("card-title")
    for(var i=0; i<encabezado.length; i++)
    {
        var celda = document.createElement('card-text');
        var textcelda = document.createTextNode(encabezados[i]);
        celda.appendChild(textcelda);
    }
    bcard.appendChild(celda);

    hcard.appendChild(bcard);
    card-deck.appendChild(hcard);
})