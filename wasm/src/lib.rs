use wasm_bindgen::prelude::*;


// --- calling javascript functions from rust ---
#[wasm_bindgen]
extern { // want to call an externally defined function
    pub fn alert(s: &str); // alert function is defined, and it takes in a string
}

// --- exporting a function to javascript ---
#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}