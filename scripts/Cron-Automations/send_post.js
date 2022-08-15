function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "app.wayscript.com", false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
