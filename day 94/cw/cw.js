function welcomeMessage(name, callback) {
    setTimeout(() => {
        console.log(`Welcome, ${name}!`);
        callback(); 
    }, 2000); 
}

function afterMessage() {
    console.log("The welcome message was displayed!");
}

welcomeMessage("John", afterMessage);