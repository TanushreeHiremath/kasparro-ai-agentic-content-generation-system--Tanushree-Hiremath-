from agents.parser_agent import parse_product
from templates.logic_blocks import (
    extract_title, extract_benefits, extract_price,
    extract_usage
)

def build_description():
    data = parse_product()

    return {
        "title": extract_title(data),
        "summary": f"{data['name']} is a Vitamin C serum designed for {', '.join(data['skin_type'])} skin types.",
        "benefits": extract_benefits(data),
        "usage": extract_usage(data),
        "price": extract_price(data)
    }
