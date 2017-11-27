data = [
  {
    "name": "Crosby",
    "age": 28,
    "points": [
      0,
      0,
      0,
      1,
      1,
      0
    ]
  },
  {
    "name": "Malkin",
    "age": 29,
    "points": [
      1,
      1,
      0,
      0,
      0,
      0
    ]
  },
  {
    "name": "Letang",
    "age": 29,
    "points": [
      1,
      0,
      1,
      0,
      1
    ]
  }
];

// output
var names = grabNames(data);
var points = grabPoints(data);
var avgs = avgAllSubArrays(points);
var pairs = combiner(names, avgs);
document.write(JSON.stringify(pairs));

// Imperative
function grabNames(arr) {
  var names = [];
  for (var i = arr.length - 1; i >= 0; i--) {
    names.push(arr[i].name);
  }
  return names;
}


function grabPoints(arr) {
  var points = [];
  for (var i = arr.length - 1; i >= 0; i--) {
    points.push(arr[i].points);
  }
  return points;
}


function avgAllSubArrays(arr) {
  var subAvgs = [];
  for (var i = 0; i < arr.length; i++) {
    subAvgs.push(average(totalAcrossArray(arr[i]), arr[i].length));
  }

  return subAvgs;
}


function totalAcrossArray(arr) {
  var total = 0;

  for (var i = arr.length - 1; i >= 0; i--) {
    total = total + arr[i]
  }

  return total;
}


function average(total, count) {
  return total/count;
}


function combiner(names, averages) {
  var combined = [];

  for (var i = names.length - 1; i >= 0; i--) {
    combined.push([names[i], averages[i]]);
  }

  return combined;
}