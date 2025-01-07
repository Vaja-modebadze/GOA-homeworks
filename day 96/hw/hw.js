let taskPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve("Task 1 complete");
    }, 2000); 
});

taskPromise.then((message) => {
    console.log(message); 
}).catch((error) => {
    console.log("Error:", error);
});