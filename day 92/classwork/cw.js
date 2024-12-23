function mergeSets(setsArray) {
    const resultSet = new Set();

    setsArray.forEach(set => {
      set.forEach(element => {
        resultSet.add(element);
      });
    });
  
    return resultSet;
  }

  const sets = [
    new Set([1, 2]),
    new Set([2, 3]),
    new Set([3, 4])
  ];
  
  const unionSet = mergeSets(sets);
  
  console.log(unionSet);