https://developer.mozilla.org/en-US/docs/WebAssembly/Rust_to_wasm#rust_environment_setup

to build the rust code:
```
wasm-pack build --target web
```

to run:

go to directory, then
```
python3 -m http.server
```

then go to `http://localhost:8000/` in browser