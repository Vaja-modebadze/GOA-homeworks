class Dog extends Animal {
    constructor(name) {
        super(name, 'Dog');  
    }

    makeSound() {
        console.log(`${this.name} barks.`);
    }
}