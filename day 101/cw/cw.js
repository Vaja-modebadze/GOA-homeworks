function characterFrequency(str) {
    const frequencyMap = new Map();
  
    for (const char of str) {
      if (frequencyMap.has(char)) {
        frequencyMap.set(char, frequencyMap.get(char) + 1);
      } else {
        frequencyMap.set(char, 1);
      }
    }
  
    return frequencyMap;
  }