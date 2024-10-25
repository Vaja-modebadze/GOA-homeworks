class Human {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
  
    get getName() {
      return this.name;
    }
  
    get getAge() {
      return this.age;
    }
  
    introduce() {
      console.log(`Hi, my name is ${this.name} and I am ${this.age} years old.`);
    }
  
    static compareAge(human1, human2) {
      return human1.age - human2.age;
    }
  }