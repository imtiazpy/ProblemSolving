// Create a Polygon class that has the following properties:

// 1.A constructor that takes an array of integer values describing the lengths of the polygon's sides.
// 2.A perimeter() method that returns the polygon's perimeter.


class Polygon {
    constructor (
        sideLength
    ) {
        this.sideLength = sideLength;    
    }
    perimeter = function() {
            let res = 0;
            for (let i=0; i<this.sideLength.length; i++) {
                res += this.sideLength[i]
            }
            return res;
        } 
}
