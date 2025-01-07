function setColorAndChangeTextColor(color, callback) {
    setTimeout(() => {
        let chosenColor = color; 
        callback(chosenColor); 
    }, 2000);
}

