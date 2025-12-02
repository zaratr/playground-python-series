import random

from rl.bandit import BernoulliBandit, EpsilonGreedyAgent


def test_bandit_pull_and_validation():
    bandit = BernoulliBandit([0.0, 1.0], rng=random.Random(0))
    assert bandit.pull(0) == 0
    assert bandit.pull(1) == 1


def test_agent_learns_best_arm():
    rng = random.Random(123)
    bandit = BernoulliBandit([0.2, 0.5, 0.8], rng=rng)
    agent = EpsilonGreedyAgent(epsilon=0.1, rng=rng)
    agent.run(bandit, steps=400)

    # The agent should strongly favor the highest-reward arm.
    assert agent.best_arm() == 2
    assert agent.counts[2] > agent.counts[0]
    assert agent.counts[2] > agent.counts[1]


def test_invalid_inputs():
    try:
        BernoulliBandit([])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty bandit")

    agent = EpsilonGreedyAgent()
    try:
        agent.initialize(0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for non-positive arms")
