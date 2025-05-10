# Project 

# 🔴🟡🟢 3-Player Connect 4 AI Game

## 📌 Project Overview
This project is a modified version of the classic Connect 4 game, transformed to support **3 players** in a turn-based format. We developed a strategic **AI opponent using Minimax with Alpha-Beta Pruning**, allowing it to make smart decisions in a multi-agent environment. This command-line Python project serves as an educational demonstration of game AI in a non-zero-sum multiplayer scenario.

---

## 🎯 Objectives
- Extend traditional 2-player Connect 4 into a **3-player game**.
- Design an **AI opponent** using the Minimax algorithm with Alpha-Beta Pruning.
- Implement **heuristics** to evaluate board states in a multiplayer setting.
- Allow **human vs AI** and **AI vs AI** gameplay.

---

## 🕹 Game Rules & Mechanics

### 🧩 Original Connect 4 Rules
- Players take turns dropping colored tokens into a 7x6 grid.
- The goal is to get **4 tokens in a row** (horizontally, vertically, or diagonally).
- The first player to do so **wins**; if the board fills without a win, it's a **draw**.

### 🔁 Modified Rules for 3 Players
- **Three players** take turns (Player 1 → Player 2 → Player 3 → ...).
- Tokens are represented numerically: Player 1 = 1, Player 2 = 2, Player 3 = 3.
- **Turn-based sequence** managed automatically.
- The game ends when **any player gets 4 in a row**, or if the board is filled → draw.

---

## 🤖 AI Approach & Methodology

### ⚙️ Algorithms Used
- **Minimax Algorithm**: Builds a game tree to choose the optimal move.
- **Alpha-Beta Pruning**: Reduces the number of nodes evaluated, improving performance.

### 📐 Heuristic Design
- Evaluates:
  - Line formations (2s and 3s in a row).
  - Central column advantage.
  - Blocking opponent threats.
  - Creating forks (double threats).

### 📊 AI Evaluation
- **Average Decision Time**: ~1–2 seconds.
- **Win Rate vs Random AI**: ~70%.
- **Handles simultaneous threats** with strategic foresight.

---

## 🛠️ Installation & Running

### 🔽 1. Clone the Repository
```bash
git clone https://github.com/junaid-shaikh2/Project.git
cd Project

