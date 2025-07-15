---
title: Rust Content
tags:
- rust
---


## Installation

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## VSCode Extensions

```bash
codium --install-extension rust-lang.rust-analyzer
codium --install-extension jscearcy.rust-doc-viewer
#1yib.rust-bundle
```

## Create New Project

```bash
cargo new exercise01
cd exercise01
cargo run
```

## Other cargo commands

```bash
cargo build --release
cargo build --debug
cargo check
```

### About ```cargo.toml```

contains dependencies

## .gitignore

```
**/target/
Cargo.lock
```

## interesting things

can use if traditionally, or as a conditional in another statemtent
continue keyword is a companion to break
you can iterate through 1..5 or lists: [1,2,3] with ```for```
match is a simplified ```switch```/```case``` statement
loop keyword just loops forever
```let``` keyword sorts out datatypes later.
last line of functions is the return if you omit the semicolon -- return can still be used
"unit type" is an empty tuple


built in functions / macros I've discovered
dbg!
println!
assert!
assert_eq!
assert_ne!
debug_assert!
mut
todo!
format!
unreachable!
eprintln! 

variables are immutable by default
constants and variables are different
```const```


## External Resources

* <https://www.rust-lang.org/learn>
* <https://github.com/google/comprehensive-rust#building>
* <https://www.w3schools.com/rust/index.php>
* <https://doc.rust-lang.org/stable/book/>
* <https://google.github.io/comprehensive-rust/running-the-course.html>
    * <https://google.github.io/comprehensive-rust/bare-metal.html>
    * <https://google.github.io/comprehensive-rust/idiomatic/welcome.html>
