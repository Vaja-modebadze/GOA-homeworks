function symmetricDifference(set1, set2) {
    const resultSet = new Set();
  
    set1.forEach(element => {
      if (!set2.has(element)) {
        resultSet.add(element);
      }
    });
  
    set2.forEach(element => {
      if (!set1.has(element)) {
        resultSet.add(element);
      }
    });
  
    return resultSet;
  }
  
  const setA = new Set([1, 2, 3]);
  const setB = new Set([3, 4, 5]);
  
  const result = symmetricDifference(setA, setB);
  
  console.log(result); 