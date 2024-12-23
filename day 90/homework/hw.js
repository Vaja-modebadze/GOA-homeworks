function removeDuplicates(arr) {
    return [...new Set(arr)];
  }
  

  const arr = [1, 2, 3, 2, 4, 5, 3];
  const uniqueArr = removeDuplicates(arr);
  console.log(uniqueArr);  