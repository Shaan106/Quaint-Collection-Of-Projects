// import init, { greet } from './pkg/wasm.js';

// async function run() {
//     await init();
//     greet('Shaan');
// }

// //func

// run();

//alternative above
import init, { greet } from "./pkg/wasm.js";
init().then(() => {
  greet("Rust WASM !!");

  // changing innerHTML of a p tag
  const p = document.getElementById("change");
  p.innerHTML = "changing inner HTML";
});
