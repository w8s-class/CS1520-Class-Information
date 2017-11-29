data = [{"name":"Crosby","age":28,"points":[0,0,0,1,1,0]},{"name":"Malkin","age":29,"points":[1,1,0,0,0,0]},{"name":"Letang","age":29,"points":[1,0,1,0,1]}];

// output
var names = getNames(data);
var points = getPoints(data);
var averages = getAverages(points);
var pairs = congregate(names, averages);
document.write(JSON.stringify(pairs));

// console.log(names);
// console.log(points);
// console.log(averages);
// console.log(pairs);

function getNames(arr) {

  var names = [];

  for (var i = 0; i < arr.length; i++) {
    names[i] = arr[i].name;
  }

  return names;
}

function getPoints(arr) {

  var points = [];

  for (var i = 0; i < arr.length; i++) {
    points[i] = arr[i].points;
  }

  return points;
}

function getAverages(arr) {
  var faverages = []
  for (var i = 0; i < arr.length; i++) {
    var total = 0;
    for (var j = 0; j < arr[i].length; j++) {
       total = total + arr[i][j];
     }
     faverages[i] = total/arr[i].length;
  }

  return faverages;
}

function congregate(nameArr, avgArr) {
  var congregation = [];

  for (var i = 0; i < nameArr.length; i++) {
    congregation[i] = [nameArr[i], avgArr[i]];
  }
  return congregation;
}












