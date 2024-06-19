


fn fn main() {
    inerstion_sort();
}


fn insertion_sort(){
    let arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
    pritnln!(arr);
    for(let j = 1; j < arr.len(); j++){
        key = arr[j];
        let i = j-1;
        while( i > 0 && arr[i] > key){
            arr[i+1] = arr[i];
            i -= 1;
        }
        A[i+1] = key;
    }
    println!(arr);
}
