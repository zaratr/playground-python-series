"""Minimal epsilon-greedy multi-armed bandit for demonstration."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Sequence


@dataclass
class BernoulliBandit:
    """Bandit environment with Bernoulli rewards for each arm."""

    probs: Sequence[float]
    rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self) -> None:
        if not self.probs:
            raise ValueError("Bandit needs at least one arm")
        if any(p < 0 or p > 1 for p in self.probs):
            raise ValueError("Probabilities must be within [0, 1]")

    def pull(self, action: int) -> int:
        if action < 0 or action >= len(self.probs):
            raise IndexError("Invalid arm index")
        return 1 if self.rng.random() < self.probs[action] else 0


@dataclass
class EpsilonGreedyAgent:
    epsilon: float = 0.1
    rng: random.Random = field(default_factory=random.Random)
    values: List[float] = field(init=False)
    counts: List[int] = field(init=False)

    def __post_init__(self) -> None:
        if not (0 <= self.epsilon <= 1):
            raise ValueError("epsilon must be in [0, 1]")

    def initialize(self, num_arms: int) -> None:
        if num_arms <= 0:
            raise ValueError("Number of arms must be positive")
        self.values = [0.0] * num_arms
        self.counts = [0] * num_arms

    def select_action(self) -> int:
        if self.rng.random() < self.epsilon or not any(self.counts):
            return self.rng.randrange(len(self.values))
        max_value = max(self.values)
        best_arms = [i for i, v in enumerate(self.values) if v == max_value]
        return self.rng.choice(best_arms)

    def update(self, action: int, reward: float) -> None:
        self.counts[action] += 1
        n = self.counts[action]
        old = self.values[action]
        # Incremental mean update
        self.values[action] += (reward - old) / n

    def run(self, bandit: BernoulliBandit, steps: int = 200) -> None:
        self.initialize(len(bandit.probs))
        for _ in range(steps):
            action = self.select_action()
            reward = bandit.pull(action)
            self.update(action, reward)

    def best_arm(self) -> int:
        return max(range(len(self.values)), key=self.values.__getitem__)
