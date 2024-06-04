from os import system
from base64 import b64encode

class Builder:
    def __init__(self, path: str) -> None:
        self.path = path

    def compile_wasm(self):
        system(f"cd assets && wat2wasm custom.wat -o ../out/custom.wasm")
        print("(+) wasm compiled!")

    def replace_wasm(self) -> None:
        with open(self.path, "rb") as f:
            b64 = b64encode(f.read()).decode("utf-8")

        with open("./assets/hsw.js", "r+", errors="ignore") as f:
            with open("./out/hsw_bind.js", "w+") as hsw:
                hsw.write(f.read().replace("!wasm!", b64))
        
        print("(+) hsw bind ready!")
    
    def run(self):
        self.compile_wasm()
        self.replace_wasm()


if __name__ == "__main__":
    Builder("./out/custom.wasm").run()