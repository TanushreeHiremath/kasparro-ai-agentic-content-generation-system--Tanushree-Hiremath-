from agents.parser_agent import parse_product

def build_comparison():
    a = parse_product()
    b = {
        "name": "GlowBoost Lite Serum",
        "concentration": "5% Vitamin C",
        "skin_type": ["All Skin Types"],
        "key_ingredients": ["Vitamin C"],
        "benefits": ["Mild brightening"],
        "how_to_use": "Apply 1 drop in the morning",
        "side_effects": "None",
        "price": "₹399"
    }

    differences = {
        "Vitamin C %": f"{a['concentration']} vs {b['concentration']}",
        "Moisture Support": "Yes (Hyaluronic Acid) vs No",
        "Price": f"{a['price']} vs {b['price']}"
    }

    return {
        "product_A": a,
        "product_B": b,
        "differences": differences
    }
