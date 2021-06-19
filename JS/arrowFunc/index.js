/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 * 
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    let newArr = [];
    for (let i=0; i<nums.length; i++) {
        
        const a = (nums[i] % 2 == 0) ? nums[i]*2:nums[i]*3
        // if (nums[i] % 2 ==0) {
        //     newArr.push(nums[i]*2)
        // }
        // else {
        //     newArr.push(nums[i]*3)
        // }
        newArr.push(a)
    }
    return newArr;
}


function main() {
    const n = +(readLine());
    const a = readLine().split(' ').map(Number);
    
    console.log(modifyArray(a).toString().split(',').join(' '));
}