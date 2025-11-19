# ♠️ Blackjack Statistics Simulator

A highly configurable and comprehensive simulation engine designed to analyze the statistical probabilities and expected values (EVs) of various decisions and rule sets in the game of Blackjack. Developed for educational and research purposes, this project allows users to simulate thousands of hands under custom rules and accurately log game data for deep statistical analysis.

## ✨ Features Overview

The simulator is built with **flexibility** and **statistical rigor** in mind, offering detailed configuration options and real-time analytics.

---

### ⚙️ Configurable Simulation Parameters

The core of the simulator is its ability to precisely model different casino rules, allowing for accurate comparison of game conditions.

* **Deck Count:** Configurable from 1 to 8 decks (with common configurations being 1-5 decks).
* **Table Seats:** Supports 1 to 7 player seats.
* **Core Rules Implementation:**
    * **Dealer Action on Soft 17 (H17/S17):** Configurable to hit (H17) or stand (S17) on a soft 17.
    * **Double After Split (DAS):** Enabled or disabled.
    * **Resplitting Aces (RSA):** Configurable limits on resplitting.
    * **Surrender:** Late surrender option can be enabled.
    * **Hole Card Peek:** Implements the dealer checking for Blackjack (when an Ace or 10-value card is exposed).
    * **Blackjack Payout:** Standard 3:2 payout is default, but customizable (e.g., 6:5).

### 📈 Live & Per-Decision Analytics

Provides players with the tools to make mathematically optimal decisions in real-time within the simulation environment.

* **Decision Outcomes:** Calculates and displays the **Win/Push/Loss odds** for the current hand/decision.
* **Expected Values (EVs):** Provides the **Action EVs** for all available moves: **Hit, Stand, Double Down, Split, and Surrender**. This is the key metric for optimal strategy evaluation.
* **Live Card Counting:** Integrates a **Running Count** and **True Count** calculator.
    * **Initial Implementation:** The widely used **Hi-Lo** system is the initial counter.
    * **Extensibility:** Designed to easily integrate other counting systems (e.g., KO, Omega II).

### 💾 Comprehensive Data Logging

Every simulation run generates a detailed dataset suitable for post-simulation analysis.

* **CSV Logging:** A comprehensive CSV file logs every critical event:
    * **Round Details:** Initial bet, deck composition.
    * **Player Decisions:** Every action taken (**Hit/Stand/Double/Split/Surrender**).
    * **Outcomes:** Final hand values, dealer hand, and financial result (**Win/Push/Loss**).
    * **Analytics:** Snapshot of the **Live Card Count** and **Action EVs** at the moment of each decision.

---

## 🚀 Getting Started

will be live when project is almost finished
