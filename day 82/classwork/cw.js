class Cat extends Animal {
    constructor(name) {
        super(name, 'Cat');  
    }
    makeSound() {
        console.log(`${this.name} meows.`);
    }
    xD() {
        console.log(`${this.name} is xD.`);
    }
}
