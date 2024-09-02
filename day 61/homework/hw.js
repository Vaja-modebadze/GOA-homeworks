const person = {
    name: "Michael",
    age: 28,
    hair_color: "back",
    hobby: "football"
};

const car = {
    model: "BMW",
    year: 2013
};

console.log(model)
console.log(year)

person.age = 30;
console.log(person.age);

function car(model, year){
    this.model = model;
    this.year = year;
}
