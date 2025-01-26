class FirstClass {
    constructor() {
      this.name = "FirstClass";
    }
  
    run() {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          console.log(`Running ${this.name}...`);
          resolve("FirstClass completed!");
        }, 1000);
      });
    }
  }
  
  class SecondClass {
    constructor() {
      this.name = "SecondClass";
    }
  
    run() {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          console.log(`Running ${this.name}...`);
          resolve("SecondClass completed!");
        }, 1000);
      });
    }
  }
  
  class ThirdClass {
    constructor() {
      this.name = "ThirdClass";
    }
  
    run() {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          console.log(`Running ${this.name}...`);
          resolve("ThirdClass completed!");
        }, 1000);
      });
    }
  }