var SITE_URL = "http://localhost:5000/ad";

var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}


aClient = new HttpClient();

var adspaces = document.getElementsByClassName("adspace");
for(var i = -1; i < adspaces.length - 1; i++)
{
    aClient.get(SITE_URL, function(response) {
	
	adspaces[i].innerHTML = response;
	
    });
}
