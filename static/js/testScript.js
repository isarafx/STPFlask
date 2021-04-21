
//single line comment

/* 
    multi lines comment
*/

var a = "10";
var b = "20";
var result = a + b;
var newA = 10;
var newB = 20;
var result2 = newA + newB;
console.log("Total1:", result);
console.log("Total2:", result2);

for(let i = 1; i<=10; i++){
    console.log("loop is running");
    console.log(i);
}

function getNum(){
    var val1 = 50;
    var val2 = 40;
    var result = val1-val2;
    console.log("result is:", result);
}

getNum();

function myFunc1(){
    document.getElementById("id1").innerHTML = "Change to STACKPYTHON";
}

function myFunc2(){
    document.getElementById("id2").style.fontSize = "140px";
}

function myFunc3(){
    var msg;
    if(confirm("You must click OK to continue or CANCEL to cancel")){
        msg = "You pressed OK"
    }
    else {
        msg = "You pressed cancel"
    }
    document.getElementById("id3").innerHTML = msg;
}