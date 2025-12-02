# War_Game


This repository contains my Python implementations of a simple card game inspired by **War**.

There will be **two versions** of the game:

1. **War Game – Single Card (war_game.py)**  
   Each player receives **one card**. The player with the highest card value wins.

2. **War Game – Multiple Cards (planned)**  
   Each player will receive **multiple cards**. The values of the cards will be **summed**, and the player with the highest total will win the round.

There is also a Jupyter notebooks where I explain the code step by step, as a way to learn Python by teaching and documenting my own work.


## Project Objectives

- Create one or more simple **card games** in Python.  
- Practice:
  - Lists and list comprehensions  
  - Dictionaries  
  - Classes  
  - Loops (`for`, `while`)  
  - Functions  
  - Basic user input  
  - The `random` and `time` modules
- Use a Jupyter notebook to explain:
  - How the code works  

## Game Versions

### War Game – Single Card (war_game.py)

- There are **2 players**.
- A standard deck of **52 cards** is used.
- Each round:
  1. Each player receives **one random card**.
  2. The values of the cards are compared.
  3. The player with the **higher value** wins.
  4. If both cards have the **same value**, it is a **draw** and both players receive a new card until someone wins.
- Cards that are dealt to players are **removed from the deck**, so they cannot appear again.

Card values used in the game:

- Number cards: `2` to `10` → value `2` to `10`  
- `Jack` → `11`  
- `Queen` → `12`  
- `King` → `13`  
- `Ace` → `14`

### War Game – Multiple Cards (planned)

This second version will be added later.

The main differences from the first version:

- Each player will receive **more than one card**.
- The numeric values of all cards in a hand will be **summed**.
- The player with the **highest total sum** will win the round.
- The goal is to reuse logic from the first version and improve the structure of the code.


