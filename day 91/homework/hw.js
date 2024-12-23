function incrementScores(studentsScores) {
    const updatedScores = new Map();
  
    for (let [student, score] of studentsScores) {
      updatedScores.set(student, score + 5);
    }
  
    return updatedScores;
  }
  
  const studentsScores = new Map([
    ['Ez', 85],
    ['Lo', 92],
    ['Xo', 78]
  ]);
  
  const updatedScores = incrementScores(studentsScores);
  
  console.log(updatedScores); 