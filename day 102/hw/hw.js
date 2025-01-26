function fetchData() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("Data fetched!");
      }, 2000);
    });
  }
  
  async function fetchAndDisplayData() {
    console.log("Fetching data...");
    const data = await fetchData();  
    console.log(data);  
  }
  
  fetchAndDisplayData();