# Python — Practice Assignments

**For candidates · Bajaj Finance Ltd. · 3-Day Course**

Short exercises following the three-day notebook, framed around everyday banking situations. Work in a notebook cell or a `.py` script on your training virtual-env. For each one: read the story, write the smallest code that produces the expected result, and predict the output before you run it.

> There's rarely one right answer — clear, working code that gives the right result is the goal.

---

## Day 1 — Types, Control, Collections

### Assignment 1 — Why money isn't a float
**Story.** A junior analyst computes a fee as `0.1 + 0.2` and is surprised the system stores `0.30000000000000004`.

**Task.** (a) Print `0.1 + 0.2` and show it does **not** equal `0.3`. (b) Redo the same sum with `Decimal` (built from strings) and show it **does** equal `Decimal("0.3")`.

**Expected output.**
```
0.30000000000000004
float equals 0.3? False
Decimal equals 0.3? True
```
**Hint.** `from decimal import Decimal`; build with `Decimal("0.1")`, not `Decimal(0.1)`.

---

### Assignment 2 — The aliasing surprise
**Story.** Two variables seem to hold "the same" transaction list, but editing one changes the other.

**Task.** Given `original = [1500, 320, 9800]`: (a) make `alias = original`, append `75` to `alias`, and show `original` changed too. (b) Make a real copy so appending to the copy leaves `original` untouched. Print `is` comparisons for both.

**Expected output.**
```
after alias append -> original: [1500, 320, 9800, 75]
alias is original? True
after copy append  -> original: [1500, 320, 9800, 75]
copy is original?  False
```
**Hint.** A real (shallow) copy: `original[:]` or `list(original)`.

---

### Assignment 3 — Four collections from one
**Story.** From a list of banks, you need the names containing the letter "a", as four different collection types.

**Task.** Given `banks = ["HDFC", "Kotak", "SBI", "ICICI", "Axis", "Bajaj Finance"]`, build and print: a **list**, a **set**, a **dict** mapping each kept name to its length, and a **tuple** — all of names containing `"a"`. Use a comprehension for the first three; build the tuple with the `tuple(...)` constructor over a generator expression.

**Expected output (set order may vary).**
```
list : ['Kotak', 'Bajaj Finance']
set  : {'Kotak', 'Bajaj Finance'}
dict : {'Kotak': 5, 'Bajaj Finance': 13}
tuple: ('Kotak', 'Bajaj Finance')
```
**Hint.** `tuple(b for b in banks if "a" in b)` — remember `(...)` is a generator expression, not a tuple comprehension. (The filter is case-sensitive, so "Axis" with a capital A is not matched.)

---

## Day 2 — Functions, Modules, Files

### Assignment 4 — A flexible summary function
**Story.** You want one function that totals any number of transaction amounts and also accepts optional labelled tags.

**Task.** Write `summarise(label, *amounts, **tags)` that prints the label, the total of the amounts, and the tags dict. Call it with three amounts and two tags.

**Expected output (example).**
```
Q1 total: 11620 tags: {'region': 'West', 'tier': 'A'}
```
**Hint.** `*amounts` packs positional args into a tuple; `**tags` packs keyword args into a dict; `sum(amounts)`.

---

### Assignment 5 — Instalments, one at a time
**Story.** A loan of ₹12,000 over 3 months should yield its instalments lazily, not all at once.

**Task.** Write a **generator** function `instalments(principal, n)` that `yield`s each instalment line. Drive it with `next()` once, then a `for` loop for the rest.

**Expected output.**
```
instalment 1: 4000.0
instalment 2: 4000.0
instalment 3: 4000.0
```
**Hint.** Use `yield` inside a loop; each amount is `principal / n`.

---

### Assignment 6 — A statement file
**Story.** Write three lines to a statement file, then read it back, safely.

**Task.** Using a **context manager** (`with`), write `"Opening: 1000"`, `"Credit: 500"`, `"Debit: 200"` (one per line) to `mini_statement.txt`. Then open it again and print it line by line with line numbers.

**Expected output.**
```
1 Opening: 1000
2 Credit: 500
3 Debit: 200
```
**Hint.** `with open(path, "w") as f:` to write; loop `for i, line in enumerate(f, 1):` to read.

---

## Day 3 — Duck Typing, Exceptions, OOP

### Assignment 7 — Pay any way
**Story.** Checkout shouldn't care *how* a customer pays — only that the payment method can `pay()`.

**Task.** Define two unrelated classes `Card` and `Wallet`, each with a `pay(amount)` method returning a distinct string. Write `checkout(method, amount)` that calls `method.pay(amount)` without checking the type. Run it with one of each.

**Expected output.**
```
Card paid 1500
Wallet paid 320
```
**Hint.** Duck typing — no `isinstance` needed; just call `.pay()`.

---

### Assignment 8 — Block the overdraft
**Story.** A withdrawal larger than the balance must raise a clear, named error that the caller can catch.

**Task.** Define a custom exception `InsufficientFundsError`. Write `withdraw(balance, amount)` that raises it when `amount > balance`, else returns the new balance. Show a successful withdrawal and a caught failure.

**Expected output.**
```
new balance: 600
blocked: need 5000, have 1000
```
**Hint.** `class InsufficientFundsError(Exception): pass`; `raise InsufficientFundsError(f"need {amount}, have {balance}")`.

---

### Assignment 9 (stretch) — Extend the account hierarchy
**Story.** Add a new account type to the family from Day 3.

**Task.** Starting from a simple `Account` (with `holder`, `balance`, and a `deposit` method), create a subclass `FixedDeposit` that (a) takes an extra `rate`, (b) adds a `mature()` method returning balance plus interest, and (c) has a `__repr__`. Create one and print a deposit, its maturity value, and its repr.

**Expected output (example).**
```
after deposit: 110000
at maturity:   118800
FixedDeposit('Riya', 110000)
```
**Hint.** Use `super().__init__(...)` in the subclass constructor; `mature()` returns `round(balance * (1 + rate))`.

---

*End of assignments. Check each output against the expected result.*
