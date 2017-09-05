data = [{"name": "Crosby", "age": 28, "points": [0, 0, 0, 1, 1, 0]}, { "name": "Malkin", "age": 29, "points": [1, 1, 0, 0, 0, 0]}, {"name": "Letang", "age": 29, "points": [1, 0, 1, 0, 1]}];

// output
var names = data.map(grabGrabAtt("name"));
var points = data.map(grabGrabAtt("points"));
var avgs = points.map(avgAcrossArray);
var pairs = combiner(names, avgs);
document.write(JSON.stringify(pairs));

// Functional

function grabGrabAtt(attName) {
	function rv (item) {
		return item[attName];
	}
	return rv;
}

function add(a, b){
	return a + b;
}

function avgAcrossArray(arr) {
	return average(arr.reduce(add), arr.length);
}

function average(total, count) {
	return total/count;
}

function combiner(arr1, arr2) {
	function combmap(e, i) {
		return [e, arr2[i]];
	}
	var result = arr1.map(combmap);
	return result;
}
