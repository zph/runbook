#!/usr/bin/env -S deno run -A

const response = prompt("What is your name?", "Doe")

console.error("debug", Deno.env.get("DEBUG"))
console.log(JSON.stringify({server: response}));
