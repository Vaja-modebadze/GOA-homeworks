let matrix = [ [1, 22, 3], [4, 55, 6], [7, 88, 9] ]; let threshold = 10; let replacement = 0;
function fixOverflowingColumns(matrix, threshold, replacement) 
{ for (let i = 0; i < matrix.length; i++)
     { for (let j = 0; j < matrix[i].length; j++) { if (matrix[i][j] > threshold) { matrix[i][j] = replacement; } } }
      return matrix; }