function countOddDigits() {
    let num = prompt("Enter an integer:");
    num = num.trim();
    let oddDigitCount = 0;
    for (let i = 0; i < num.length; i++) {
        let digit = parseInt(num[i], 10);
        if (digit % 2 !== 0) {
            oddDigitCount++;
        }
    alert("The number contains " + oddDigitCount + " odd digits.");
}


    countOddDigits();
    }