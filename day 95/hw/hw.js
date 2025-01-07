function promptAndCongratulate() {
    let userName = prompt("enter your name:");

    setTimeout(() => {
        alert(`Congratulations, ${userName}! Thank you for helping!`);
    }, 3000); 
}

promptAndCongratulate();