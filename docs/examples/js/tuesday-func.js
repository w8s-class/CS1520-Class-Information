data = [{ "name": "Crosby", "age": 28, "points": [0, 0, 0, 1, 1, 0] }, { "name": "Malkin", "age": 29, "points": [1, 1, 0, 0, 0, 0] }, { "name": "Letang", "age": 29, "points": [1, 0, 1, 0, 1] }];

// output
var pairs = data.filter(checkAge(28)).map(combiner)
document.write(JSON.stringify(pairs));

function checkAge(age) {
    return function(item, idx, arr) {
        return item.age < age;
    }
}

function combiner(item, idx, arr) {
    return [item.name, item.points.reduce(totalAcrossArray, 0) / item.points.length];
}
// Imperative
function avgAllSubArrays(item, idx, arr) {
    return item.reduce(totalAcrossArray, 0) / item.length;
}

function totalAcrossArray(agg, item, idx, arr) {
    return agg + item;
}