function uniqueInOrder(sequence){
    const result = [];
    let lastItem;
    
    for(let i = 0; i < sequence.length; i++){
      if(sequence[i] != lastItem){
        result.push(sequence[i]);
        lastItem = sequence[i]
      }
    }
    
    return result;
  }

// ფუნქცია რომელიც არის მოცემული არის შექმნილი იმისათვის, რომ ამოიღოს მიყოლებითი ნივთები მიმდევრობიდან.