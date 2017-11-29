data = [{"name":"Crosby","age":28,"points":[0,0,0,1,1,0]},{"name":"Malkin","age":29,"points":[1,1,0,0,0,0]},{"name":"Letang","age":29,"points":[1,0,1,0,1]}];

var names = getNames(data);
var scores = getScores(data);
var averages = getAverages(scores);
var pairs = whenTwoBecomeOne(names, averages);
document.write(JSON.stringify(pairs));

console.log(names);
console.log(scores);
console.log(averages);
console.log(pairs);

function getNames(arr) {
    var nameArr = [];

    for (var i = 0; i < arr.length; i++) {
        nameArr.push(arr[i].name);
    }

    return nameArr;
}

function getScores(arr) {
    var scoreArr = [];

    for (var i = 0; i < arr.length; i++) {
        scoreArr.push(arr[i].points);
    }

    return scoreArr;
}

function getAverages(arr) {
    var averageArr = []

    for (var i = 0; i < arr.length; i++) {
        var sum = 0;
        for (var j = 0; j < arr[i].length; j++) {
            sum = sum + arr[i][j];
        }

        averageArr.push(sum/arr[i].length);
    }

    return averageArr;
}

function whenTwoBecomeOne(nameArr, averageArr) {
    var pairReturn = [];
    for (var i = 0; i < nameArr.length; i++) {
        pairReturn.push([nameArr[i], averageArr[i]]);
    }

    return pairReturn;
}



















