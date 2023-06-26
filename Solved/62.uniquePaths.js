/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */

var uniquePaths = function(m, n) {
    let curr = Array(m+1).fill(0)
    let prev = Array(m+1).fill(0)

    curr[m-1] = 1
    let index = m-2;

    while (n>0) {
        while (index >= 0) {
            curr[index] = curr[index+1] + prev[index];
            --index;
        }
        --n;
        index = m-1;
        prev = curr;
    }
    return curr[0];
};
