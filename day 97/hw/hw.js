function firstThenSecond() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("First"); 
        }, 2000);
    });
}

firstThenSecond()
    .then((message) => {
        console.log(message);
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve("Second"); 
            }, 1000);
        });
    })
    .then((message) => {
        console.log(message); 
    })
