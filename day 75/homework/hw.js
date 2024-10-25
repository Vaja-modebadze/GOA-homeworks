class Animal {
    constructor(name) {
      this.name = name;
    }
  
    speak() {
      console.log(`${this.name} makes a sound.`);
    }
  }

  class Dog extends Animal {
    speak() {
      console.log(`${this.name} barks.`);
    }
  }

  class Vehicle {
    constructor(make) {
      this.make = make;
    }
 }
    

  class Car extends Vehicle {
    move() {
      console.log(`${this.make} car is driving.`);
    }
  }