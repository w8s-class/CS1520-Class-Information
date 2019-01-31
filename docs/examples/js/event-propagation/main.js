var state = [];
var animationElement = null;
var t = 1;

var eventOrder = [];

var bus = new Image();
bus.src = "img/bus.png";
bus.width = 30;
bus.height = 30;
bus.id = "bus";

function getStateElement(id) {
    return function(item) {
        return item.id === id;
    }
}

function animateCapturePhase() {
    var a = document.getElementById('animate');
    if (document.getElementById('bus')) {
        var elem = document.getElementById('bus');
    } else {
        var elem = a.appendChild(bus);
    }
    elem.style.position = 'absolute';
    var y = 0;
    var x = 90;

    var id = setInterval(frame, 5);

    function frame() {
        if (y == 150 && x == 180) {
            clearInterval(id);
        } else if (y == 150) {
            x++;
            elem.style.top = y + 'px';
            elem.style.left = x + 'px';
        } else {
            y++;
            elem.style.top = y + 'px';
            elem.style.left = x + 'px';
        }
    }

    getEventOrder(false);
}

function animateBubblePhase() {

    var a = document.getElementById('animate');
    if (document.getElementById('bus')) {
        var elem = document.getElementById('bus');
    } else {
        var elem = a.appendChild(bus);
    }
    elem.style.position = 'absolute';
    var y = 150;
    var x = 180;

    var id = setInterval(frame, 5);

    function frame() {
        if (y == 0 && x == 180) {
            clearInterval(id);
        } else {
            y--;
            elem.style.top = y + 'px';
            elem.style.left = x + 'px';
        }
    }

    getEventOrder(true);
}

function getEventOrder(bubble) {
    document.getElementById('event-order').innerHTML = "";
    eventOrder = [];
    var obj = state.filter(getStateElement(select.selectedOptions[0].value))[0];

    var captureEvents = obj.parents.filter(function(item) {
        return item.getCapture();
    })
    eventOrder = eventOrder.concat(captureEvents);

    if (bubble) {
        var bubbleEvents = obj.parents.filter(function(item) {
            return typeof item.getCapture() === 'boolean' && !item.getCapture();
        }).reverse();
        eventOrder = eventOrder.concat(bubbleEvents);
    }
    console.log(eventOrder);

    var ol = document.getElementById('event-order');

    for (var i = 0; i < eventOrder.length; i++) {
        var li = document.createElement('li');
        li.textContent = eventOrder[i].tag + "#" + eventOrder[i].id + " - " + eventOrder[i].getCapture();
        ol.appendChild(li);
    }
}

function ElementInfo(el) {
    this.tag = el.tagName.toLowerCase();
    this.id = el.id;
    this.listeners = [];
    this.parents = [this];

    this.getParentString = function() {
        return this.parents.map(item => item.tag).join(' > ')
    }

    this.getListenerString = function() {
        return this.listeners.map(item => "Event: '" + item.event + "' Capture: " + item.capture).join(', ')
    }

    this.getCapture = function() {
        if (this.listeners.length > 0) {
            return this.listeners[0].capture;
        }
        return null;
    }

    var p = el.parentNode;
    while (p) {
        if (p instanceof HTMLElement) {
            var tmp = state.filter(getStateElement(p.id))[0];
            if (tmp == null) {
                tmp = new ElementInfo(p);
            }
            this.parents.unshift(tmp);
        }
        p = p.parentNode;
    }
}

function createDefinitionTerm(term, def) {
    var elTerm = document.createElement('dt');
    var elDef = document.createElement('dd');
    elTerm.textContent = term;
    elDef.textContent = def;

    return [elTerm, elDef]
}

function addEventListenerWrapper(el, eventName, func, useCapture) {
    el.addEventListener(eventName, func, useCapture);
    var ei = state.filter(getStateElement(el.id))[0];
    if (ei == null) {
        ei = new ElementInfo(el);
    }
    ei.listeners.push({ event: eventName, capture: useCapture });
    state.push(ei);
}