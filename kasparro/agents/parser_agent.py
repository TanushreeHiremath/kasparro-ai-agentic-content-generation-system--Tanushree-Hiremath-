import json
import os

def parse_product():
    path = os.path.join("data", "product.json")
    with open(path) as f:
        return json.load(f)

if __name__ == "__main__":
    print(parse_product())
