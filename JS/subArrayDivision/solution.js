const birthday = (s, d, m) => {
    let segment_count = 0

    for (let i = 0; i <= s.length; i++) {
        if ((s.slice(i, m+i)).reduce((a, b) => a + b, 0) == d) {
            segment_count += 1
        }
    }
    return segment_count
}
    

// const s = [1, 2, 1, 3, 2]
// const m = 2
// const d = 3
// const x = birthday(s, d, m)

// console.log(x)