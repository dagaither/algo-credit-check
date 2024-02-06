let singles = [];

function creditCheck(str) {
    for (let i = str.length - 1; i >= 0; i -= 2) {
        singles.push(parseInt(str[i]));
    }

    for (let i = str.length - 2; i >= 0; i -= 2) {
        let num = parseInt(str[i]) * 2;

        if (num < 9) {
            singles.push(num); 
        } else {
            num = Math.floor(num / 10) + (num % 10);
            singles.push(num);
        }
    }
    let sum = 0;
    singles.forEach(num => {
        sum += num;
    })

    if (sum % 10 == 0) {
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }
}

module.exports = creditCheck;