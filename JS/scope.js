
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
