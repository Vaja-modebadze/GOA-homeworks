function bubbleSort(arr) {
    let n = arr.length;
    
    for (let i = 0; i < n - 1; i++) {
       
        let swapped = false;
        for (let j = 0; j < n - 1 - i; j++) {    
            if (arr[j] > arr[j + 1]) {    
                let temp = arr[j];
                swapped = true;
            }
        }

        if (!swapped) {
            break;
        }
    }

    return arr;
}


       
        