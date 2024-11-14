function generateVariations(n) 
{ let variations = []; for (let i = 1; i < n; i++) 
    { for (let j = i + 1; j <= n; j++) { variations.push([i, j]); } 
    } return variations; 
    }

let number = 5; console.log(generateVariations(number));