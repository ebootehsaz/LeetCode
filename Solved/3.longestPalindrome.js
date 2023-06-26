/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let end = 0;
    let start = 0;

    for (let i = 0; i < s.length; ++i) {
        let res = palindromeLengthAndStartIndex(s, i);
        if (res[0] > end-start) {
            start = res[1];
            end = res[0] + res[1];
        }
    }

    return s.substring(start, end);

};


/**
 * @param {string} s
 * @return {number[]}
 */
var palindromeLengthAndStartIndex = function(s, index) {
    const length = s.length;

    let i = index;
    let j = index+1;
    // even
    let even = 0;
    let evenIndex = i;
    while (i >= 0 && j < length && s[i] === s[j]) {
        even = even + 2;
        evenIndex = i;
        --i;
        ++j;
        
    }

    i = index-1;
    j = index+1;
    // odd
    let odd = 1;
    let oddIndex = index;
    while (i >= 0 && j < length && s[i] === s[j]) {
        odd = odd + 2;
        oddIndex = i;
        --i;
        ++j;
    }

    if (even > odd) {
        return [even, evenIndex];
    } 
    return [odd, oddIndex];
    
}