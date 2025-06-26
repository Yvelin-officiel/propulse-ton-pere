TARGET_PATH=simeis-server.exe

build:
	cargo build

release:
	set RUSTFLAGS=-C code-model=kernel && cargo build --release

optimize:
	strip target/release/${TARGET_PATH}
