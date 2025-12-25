import json, os
from agents.faq_agent import build_faq
from agents.description_agent import build_description
from agents.comparison_agent import build_comparison

OUTPUT = "example_outputs"

def save(name, data):
    os.makedirs(OUTPUT, exist_ok=True)
    with open(os.path.join(OUTPUT, name), "w") as f:
        json.dump(data, f, indent=4)
    print(f" Saved: {name}")

def run_faq(): save("faq.json", build_faq())
def run_description(): save("product_page.json", build_description())
def run_comparison(): save("comparison.json", build_comparison())

def run_all():
    run_faq(); run_description(); run_comparison()
