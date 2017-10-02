var timeoutID;
var timeout = 1000;

function setup() {
	document.getElementById("theButton").addEventListener("click", addTodo, true);

	poller();
}

function makeReq(method, target, retCode, action, data) {
	var httpRequest = new XMLHttpRequest();

	if (!httpRequest) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}

	httpRequest.onreadystatechange = makeHandler(httpRequest, retCode, action);
	httpRequest.open(method, target);
	
	if (data){
		httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		httpRequest.send(data);
	}
	else {
		httpRequest.send();
	}
}

function makeHandler(httpRequest, retCode, action) {
	function handler() {
		if (httpRequest.readyState === XMLHttpRequest.DONE) {
			if (httpRequest.status === retCode) {
				console.log("recieved response text:  " + httpRequest.responseText);
				action(httpRequest.responseText);
			} else {
				alert("There was a problem with the request.  you'll need to refresh the page!");
			}
		}
	}
	return handler;
}

function addTodo() {
	var newDo = document.getElementById("newDo").value
	var data;
	data = "task=" + newDo;
	window.clearTimeout(timeoutID);
	makeReq("POST", "/todos", 201, poller, data);
	document.getElementById("newDo").value = "New ToDo Item";
}

function poller() {
	makeReq("GET", "/todos", 200, repopulate);
}

function deleteTodo(taskID) {
	makeReq("DELETE", "/todos/" + taskID, 204, poller);
}

// helper function for repop:
function addCell(row, text) {
	var newCell = row.insertCell();
	var newText = document.createTextNode(text);
	newCell.appendChild(newText);
}

function repopulate(responseText) {
	console.log("repopulating!");
	var todos = JSON.parse(responseText);
	var tab = document.getElementById("theTable");
	var newRow, newCell, t, task, newButton, newDelF;

	while (tab.rows.length > 0) {
		tab.deleteRow(0);
	}
			
	for (t in todos) {
		newRow = tab.insertRow();
		addCell(newRow, t);
		for (task in todos[t]) {
			addCell(newRow, task);
			addCell(newRow, todos[t][task]);
		}
		
		newCell = newRow.insertCell();
		newButton = document.createElement("input");
		newButton.type = "button";
		newButton.value = "Delete " + t;
		(function(_t){ newButton.addEventListener("click", function() { deleteTodo(_t); }); })(t);
		newCell.appendChild(newButton);
	}

	timeoutID = window.setTimeout(poller, timeout);
}

// setup load event
window.addEventListener("load", setup, true);
