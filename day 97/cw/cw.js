let numberPromise = new Promise((resolve, reject) => {
    resolve(5); 
});

numberPromise
    .then((number) => {
        console.log("Initial number:", number); 
        return number * 2; 
    })
    .then((doubledNumber) => {
        console.log("Doubled number:", doubledNumber); 
    })
    .catch((error) => {
        console.log("Error:", error);
    });