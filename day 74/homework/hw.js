class Worker extends Human {
    constructor(name, age, job) {
      super(name, age);
      this.job = job;
    }
  
    introduce() {
      console.log(`Hi, my name is ${this.name}, I am ${this.age} years old and I work as a ${this.job}.`);
    }
}