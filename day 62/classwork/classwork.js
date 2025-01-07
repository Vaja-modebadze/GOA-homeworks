function Animal(name, sound) {
    this.name = name;   
    this.sound = sound; 
    
    this.makeSound = function() {
        console.log(this.sound); 
    };
}


