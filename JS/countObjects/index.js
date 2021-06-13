// Complete the function in the editor. It has one parameter: an array,'a', of 
// objects. Each object in the array has two integer properties denoted by  
// 'X' and 'Y'. The function must return a count of all such objects 'o' 
// in array 'a' that satisfy o.x == o.y  



function getCount(objects) {

    // complete the function
    let counts = 0;
    for (let i=0; i<objects.length; i++) {
        if (objects[i]['x'] == objects[i]['y']) {
            counts+=1
        }
    }
    return counts;
}


function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}