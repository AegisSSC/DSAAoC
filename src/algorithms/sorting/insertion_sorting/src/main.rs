fn main() {
    println!("Hello, world!");
    insertion_sort();
}


fn insertion_sort(){
    let mut arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
    println!("Beginning array is: ");
    for x in arr {
        print!("{x} ");
    }
    print!("\n");
    for i in 1..arr.len() {
    
        println!("i = {i}. i at arr[{i}] = {val}", val = arr[i]);
        let key = arr[i];
        let mut j = i;
        while j > 0 && arr[j-1] > key {
            arr[j] = arr[j-1];
            j -= 1;
        }
        arr[j] = key;
    }
    println!("Ending array is:");
    for x in arr{
        print!("{x} ");
    }
}

