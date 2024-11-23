class Animal { constructor(name, species)
    { this.name = name; this.species = species; }
    describe() { return `${this.name} is a ${this.species}.`; } }

class Dog extends Animal { constructor(name, breed) 
    { super(name, 'Dog'); }}


   