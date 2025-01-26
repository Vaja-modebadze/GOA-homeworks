function unionOfSets(setsArray) {
    const unionSet = new Set();
  
    for (const set of setsArray) {
      for (const item of set) {
        unionSet.add(item);
      }
    }
  
    return unionSet;
  }