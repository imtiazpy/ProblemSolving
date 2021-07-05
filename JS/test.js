/*
// let is a blocked scope
for (let i=1; i<5; i++) {
    setTimeout(() => {
        console.log(i);
    }, i * 1000);
}


// var is a global scope
for (var i=1; i<5; i++) {
    setTimeout(() => {
        console.log(i);
    }, i * 1000);
}
*/
// const arr = ['a', 'b', 'c']
// for (let i=0; i<arr.length; i++) {
//     setTimeout(() => {
//         console.log(arr[i]);
//     }, i*1000);
// }


// for (let i=arr.length; i>=0; i--) {
//     setTimeout(() => {
//         console.log(arr[i]);
//     }, i*1000);
// }


// trying some closures thing

function greet() {
    function helper() {
        // let name;
    }
    // helper()
    name = "Mr X"
    console.log(name)
}

greet()