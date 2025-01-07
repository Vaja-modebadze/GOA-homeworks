function printMessageWithDelay(message, callback) {
    setTimeout(() => {
        console.log(message);  
        callback(); 
    }, 2000); 
}

function checkIfFinished() {
    console.log("The process has finished!");
}

printMessageWithDelay("This is your message!", checkIfFinished);