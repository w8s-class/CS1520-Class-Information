data = [{"name":"Crosby","age":28,"points":[0,0,0,1,1,0]},{"name":"Malkin","age":29,"points":[1,1,0,0,0,0]},{"name":"Letang","age":29,"points":[1,0,1,0,1]}];

// output
var names = data.map(getAttr("name"));
var points = data.map(getAttr("points"));
var averages = getAverages(points);
var pairs = averages.map(congregate(names));
document.write(JSON.stringify(pairs));

console.log(names);
console.log(points);
console.log(averages);
console.log(pairs);

function getAttr(attrName) {
    function attrGetter(item) {
        return item[attrName];
    }
    return attrGetter;
}

function getAverages(arr) {
  return arr.map(subAverages);
}

function subAverages(item) {
    return average(item.reduce(add), item.length);
}

function add(a, b) {
    return a+b;
}

function average(total, count) {
    return total/count;
}

function congregate(nameArr) {
  function congregation(item, index) {
    return [nameArr[index],item];
  }
  return congregation;
}












