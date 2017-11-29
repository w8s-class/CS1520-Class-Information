data = [{"name":"Crosby","age":28,"points":[0,0,0,1,1,0]},{"name":"Malkin","age":29,"points":[1,1,0,0,0,0]},{"name":"Letang","age":29,"points":[1,0,1,0,1]}];

var names = data.map(getAttr("name"));
var scores = data.map(getAttr("points"));
var averages = scores.map(getAverages);
var pairs = averages.map(whenTwoBecomeOne(names));
document.write(JSON.stringify(pairs));

console.log(names);
console.log(scores);
console.log(averages);
console.log(pairs);

function getAttr(attr) {
    function mapGetAttr(item) {
        return item[attr];
    }
    return mapGetAttr;
}

function getAverages(arr) {
    return average(arr.reduce(sum), arr.length);
}

function sum(a, b) {
    return a+b;
}

function average(total, count) {
    return total/count;
}

function whenTwoBecomeOne(nameArr) {
  function congregation(item, index) {
    return [nameArr[index],item];
  }
  return congregation;
}



















