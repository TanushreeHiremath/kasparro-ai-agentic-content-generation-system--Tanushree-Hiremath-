## Problem Statement

- The assignment requires building a **modular, agent-driven automation system** that can take a **JSON-like product dataset** and automatically generate **structured JSON content pages**.
- The system must **not** be a single-script GPT wrapper. Instead, it should be built using **multiple independent components (agents)**, reusable logic blocks, and a **template-based content-generation workflow**, demonstrating clear system-design ability rather than just prompt usage.

## Solution Overview

The solution is a modular, multi-agent Python system that runs locally and automatically creates structured JSON files using the provided product information. Instead of writing one long script, the system is broken into smaller parts (agents), where each agent has only one job. This makes the design clean, reusable, and easy to understand.

### What the System Generates

When the system runs, it produces three JSON files:

- **faq.json** – contains 15 categorized FAQ question-and-answer pairs about the product
- **product_page.json** – contains the product summary, benefits, usage instructions, and price
- **comparison.json** – compares GlowBoost Serum with a fictional simplified version called “GlowBoost Lite Serum”

All generated files are saved automatically inside the `example_outputs/` folder.

### How the System Works

Below is a short explanation of how each part of the system contributes:

- A **parser agent** reads the product data from `product.json`
- A **question agent** creates 15 categorized questions
- A **FAQ agent** takes those questions and generates answers using rule-based logic
- A **description agent** creates a small product description page
- A **comparison agent** creates a fake Product-B and then compares both products
- A **logic blocks file** contains helper functions (like extract usage, price, ingredients, etc.)
- A **template engine** fills templates using the logic blocks
- An **orchestrator** controls which agent runs and ensures the right file is created

### Why This Design Was Chosen

Breaking the logic into multiple agents shows:

- The project is **not a single GPT wrapper**, but a real engineered pipeline
- Parts of the system are **reusable** and can support more products in the future
- Each agent can be tested separately
- The project is **easy to understand**
- It still proves **automation and system design skills**

## Scope & Assumptions

### Scope of the Project

This project is designed to complete the requirements of the Kasparro Applied AI Engineer challenge. The focus of the system is on:

- Reading one JSON-based product dataset
- Automatically generating structured JSON content using a multi-agent design
- Producing three output pages (FAQ, Product Page, Comparison)
- Demonstrating modular system design, reusable logic, and automation

### Assumptions

To ensure clarity, the following assumptions are made:

- The product dataset format **will not change**
- The fictional comparison product is created using only the same schema as the original dataset
- No additional skincare information should be added that is not already present in the dataset
- The goal is to **prove system-design ability**, not AI content creativity

## system design

The user starts the system by running main.py file

main.py does not generate any JSON by itself.
Its only job is to display a menu and capture the user’s choice, for example:
1 – Generate FAQ Page
2 – Generate Product Page
3 – Generate Comparison Page
4 – Generate All
5 – Exit
Once the user selects an option, main.py sends this instruction to the orchestrator.

User
 │
 │ runs
 ▼
main.py   →  collects input & passes to orchestrator
 │
 ▼
orchestrator.py  → decides which agent must run
 │
 ├── parser_agent.py → loads product.json
 │
 ├── faq_agent.py → uses logic_blocks + template_engine → faq.json
 │
 ├── description_agent.py → template_engine → product_page.json
 │
 └── comparison_agent.py → logic_blocks → comparison.json
