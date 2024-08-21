let counter = 0;
const incrementBtn = document.getElementById('increment-btn');
incrementBtn.addEventListener('click', () => {
    counter++;
    counterValue.textContent = counter;
});

