
// bring the io library from the standard library into scope
use std::io;

//random number generation
use rand::Rng;

//comparing
use std::cmp::Ordering;

//main func is entry point of program
fn main() {

    //println! is a macro that prints a string to the screen
    // -- what is a macro?
    println!("Guess the number");

    //rnd num is immutable 
    // 1..=100 inclusive range 1-100
    let secret_number = rand::thread_rng().gen_range(1..=100);


    loop {

        println!("Enter a number:");

        
        // rust variables are immutable by default
        //mut keyword makes the variable mutable
        //string type provided by the standard library that is a growable, UTF-8 encoded bit of text.
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        //convert to int type to allow for comparision
        // reusing a name is called shadowing

        //using a match statement on result type returned by parse
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
                            

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small."),
            Ordering::Greater => println!("Too big."),
            Ordering::Equal => {
                println!("Correct.");
                break;
            }
            
            
            
        }

    }
    
} 