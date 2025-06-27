TARGET_PATH=simeis-server.exe
all: check test release optimize manual

build:
	cargo build

release:
	set RUSTFLAGS=-C code-model=kernel && cargo build --release

optimize:
	strip target/release/${TARGET_PATH}

manual:
	typst compile doc/manual.md manuel.pdf

check:
	cargo check

test:
	cargo test

clean:
	cargo clean

format:
	cargo fmt --check

schema:
	cargo clippy
