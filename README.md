# monte-carlo-blackjack
Reinforcement learning project using Monte Carlo control to learn optimal Blackjack strategy.

# 🃏 Monte Carlo Blackjack — On-Policy MC Control

**One-liner:** A from-scratch implementation of **on-policy Monte Carlo control (ε-greedy)** that learns a hit/stand policy for Blackjack and beats random play, approaching basic strategy under matched rules.

---

## 🔍 Problem & Rules

**Goal:** Learn an action policy π(s) for **hit/stand** that maximizes expected return.

**Rules used (for reproducibility):**
- 6-deck shoe; reshuffle when penetration threshold is reached (e.g., 75%)
- Dealer **stands on soft 17**
- No splits, no doubles (focus purely on hit/stand)
- (If implemented) Natural blackjack pays 3:2

**State representation (classic):**
- `player_sum` ∈ [4..21]
- `dealer_upcard` ∈ {A,2,…,10}
- `usable_ace` ∈ {True, False}

**Actions:** `hit` or `stand`

---

## 🧠 Method (MC Control)

- **On-policy Monte Carlo** with **ε-greedy** exploration  
- Estimate **Q(s,a)** from episodic returns (first-visit or every-visit)  
- Policy improvement via **greedy(Q)** as ε decays

**Baselines:** Random policy and a rules-matched Basic Strategy (no splits/doubles).

---

## 🚀 How to Run (Menu-driven)

Run the script and pick an option from the menu:

python monte_carlo_blackjack.py

You will see:
================= Monte Carlo Blackjack =================
1) Play interactively
2) Train (then save Q to q_table.pkl)
3) Evaluate from saved Q (q_table.pkl)
4) Show policy table from saved Q
5) Train + Evaluate
0) Exit
========================================================
Select an option: 

What each option does

1) Play interactively

Human vs dealer. Handy to sanity-check rules (hit/stand logic, soft 17, reshuffle, etc.).

No Q-table needed.

2) Train (save Q to q_table.pkl)

Runs on-policy Monte Carlo control with ε-greedy exploration.

At the end, saves q_table.pkl (pickle of your Q[(state, action)] or equivalent).

Recommended to also write metrics/plots to ./results/ (learning curve, returns, etc.).

3) Evaluate from saved Q (q_table.pkl)

Loads the saved Q-table and runs N evaluation hands (e.g., 100k).

Prints win / push / loss rates and (optionally) saves a JSON/CSV to ./results/.

4) Show policy table from saved Q

Loads q_table.pkl, computes greedy policy, and prints/plots policy tables:

Hard totals vs dealer upcard

Soft totals (usable ace) vs dealer upcard

Optionally outputs PNGs to ./results/:

policy_heatmap_usable_ace.png

policy_heatmap_no_ace.png

5) Train + Evaluate

Runs training → saves q_table.pkl → immediately evaluates on a fixed eval set.

Great for quick experiments you can screenshot for the README / LinkedIn.

Default paths:

Q-table file: q_table.pkl at the project root (or ./results/q_table.pkl).

Figures/metrics: ./results/ (create this folder if it doesn’t exist).
