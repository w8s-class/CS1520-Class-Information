data = [{ "name": "Crosby", "age": 28, "points": [0, 0, 0, 1, 1, 0] }, { "name": "Malkin", "age": 29, "points": [1, 1, 0, 0, 0, 0] }, { "name": "Letang", "age": 29, "points": [1, 0, 1, 0, 1] }];


var pairs = data.filter(lessThanAge(29)).map(combiner)

document.write(JSON.stringify(pairs));

// Functional
function combiner(item, idx, arr) {
    return [item.name, item.points.reduce(totalAcrossArray, 0) / item.points.length];
}

function lessThanAge(age) {
    return function(item, idx, arr) {
        return item.age < age;
    }
}

function totalAcrossArray(agg, item, idx, arr) {
    return agg + item;
}