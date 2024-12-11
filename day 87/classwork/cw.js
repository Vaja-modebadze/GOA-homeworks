const countriesAndCapitals = new Map([
    ["France", "Paris"],
    ["Japan", "Tokyo"],
    ["Canada", "Ottawa"]
]);

countriesAndCapitals.forEach((capital, country) => 
    console.log(`The capital of ${country} is ${capital}.`))
