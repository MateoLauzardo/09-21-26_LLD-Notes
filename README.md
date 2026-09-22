# Low Level Design

This is where I keep the low level design (LLD) work I study.

Each file is one concept — Python OOP fundamentals: enums, interfaces, and the four
object relationships (composition, aggregation, association, dependency). The prompts
live in `questions/` as plain text files, one per concept, and I write my solutions in
the `.py` files at the root. Most problems also ask for the time and space complexity
with a rationale, so the answers are written out in comments next to the code. I post
about these same questions daily on my YouTube channel, where I walk through my thinking
and work the problems out loud.

YouTube: https://www.youtube.com/@MTZTrades

## Files

`questions/`

- `enums.txt` – parsing raw input into enum members, counting by status
- `interfaces.txt` – abstract base classes, coding to an interface, SOLID
- `composition.txt` – the whole builds and owns its parts
- `aggregation.txt` – the parts outlive the whole
- `association.txt` – two-way links that stay in sync
- `dependency.txt` – injecting a strategy instead of constructing one
- `capstone.txt` – vending machine using all six concepts (do this one last)

Solutions

- `enums.py` – `parse_vehicle_type()` and `count_by_status()`
- `interfact.py` – interfaces, in progress
