// 1
const numbers = [1, 2, 3];

numbers.forEach(number => {
  console.log(number);
});
// 2
const numbers = [1, 2, 3, 4, 5];
let sum = 0;

numbers.forEach(number => {
  sum += number;
});

console.log(sum); 
// 3
const studentNames = ['Ice', 'Bb', 'Char', 'Dia'];

studentNames.forEach(name => {
  console.log(`Student Name: ${name}`);
});
// 4
const integers = [1, 2, 3, 4, 5];
const doubled = [];

integers.forEach(number => {
  doubled.push(number * 2);
});

console.log(doubled); 
// 5
const numbers = [1, 3, 6, 9];
const squares = numbers.map(number => number * number);

console.log(squares); 
