function Scores(studentsScores) {
    const updatedScores = new Map();
    
    for (let [student, score] of studentsScores) {
      updatedScores.set(student, score + 5);
    }
  
    return updatedScores;
  }
  