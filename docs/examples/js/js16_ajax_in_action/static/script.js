function setup() {
	document.getElementById("theButton").addEventListener("click", makePost, true);
}

function makePost() {
	var httpRequest = new XMLHttpRequest();

	if (!httpRequest) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}
			
	httpRequest.onreadystatechange = function() { alertResult(httpRequest) };
	
	httpRequest.open("POST", "/new_item");
	httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

	var data;
	data = "one=" + document.getElementById("a").value + "&two=" + document.getElementById("b").value + "&three=" + document.getElementById("c").value;
	
	httpRequest.send(data);
}

function alertResult(httpRequest) {
	alert("ALERTING!  readyState:  " + httpRequest.readyState);
	if (httpRequest.readyState === XMLHttpRequest.DONE) {
		alert("ALERTING!  status:  " + httpRequest.status);
		if (httpRequest.status === 200) {
			alert("ALERTING!  Value sent to server!");
		} else {
			alert("ALERTING!  There was a problem with the request.");
		}
	}
}

window.addEventListener("load", setup, true);
