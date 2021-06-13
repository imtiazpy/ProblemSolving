function onButton(e) {
    var btn = e.target || e.srcElement;
    var action = document.getElementById(btn.id).innerHTML;
    var res = document.getElementById('res');

    switch(action) {
        case '0':
        case '1':
        case '+':
        case '-':
        case '*':
        case '/':
            res.innerHTML += action;
            break;
        case 'C':
            res.innerHTML = '';
            break;
        case '=':
            var expr = res.innerHTML;
            var nums = /(\d+)/g;
            // Replace all base 2 nums with base 10 equivs
            expr = expr.replace(nums, function(match) {
                return parseInt(match, 2);
            })
            // eval in base 10 and convert to base 2
            res.innerHTML = Math.floor(eval(expr)).toString(2);
            break;
        default:
            console.error('should not be executed');
            break;
    }
}
var buttons = document.getElementsByTagName('button');
for (let button of buttons) {
    button.onclick = onButton;
}













// const btn0 = document.getElementById('#btn0');
// const btn1 = document.getElementByI('#btn1');
// const btnClr = document.getElementBId('#btnClr');
// const btnEql = document.getElementByI('#btnEql');
// const btnSum = document.getElementByI('#btnSum');
// const btnSub = document.getElementByI('#btnSub');
// const btnMul = document.getElementByI('#btnMul');
// const btnDiv = document.getElementByI('#btnDiv');


// const action = function(e) {
//     const btn = e.target || e.srcElement;

//     document.getElementById('res').innerHTML = document.getElementById('#btn1').innerHTML;
// 


// document.getElementById('btn1').addEventListener('click', action);













// const btn = document.getElementById("btn1");
// btn.onclick = function() {
//     document.getElementById("res").innerHTML++
// 

