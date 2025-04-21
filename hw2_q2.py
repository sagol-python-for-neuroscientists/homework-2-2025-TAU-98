from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def improve(agent):
    if agent.category == Condition.DYING:
        return Agent(agent.name, Condition.SICK)
    if agent.category == Condition.SICK:
        return Agent(agent.name, Condition.HEALTHY)
    return agent

def worsen_pair(a1, a2):
    def worsen(cat):
        if cat == Condition.SICK:
            return Condition.DYING
        if cat == Condition.DYING:
            return Condition.DEAD
        return cat

    return [
        Agent(a1.name, worsen(a1.category)),
        Agent(a2.name, worsen(a2.category))
    ]

def resolve_meeting(agent1, agent2):

    if agent1.category in {Condition.HEALTHY, Condition.DEAD} or agent2.category in {Condition.HEALTHY, Condition.DEAD}:
        return [agent1, agent2]


    if agent1.category == Condition.CURE:
        return [agent1, improve(agent2)]
    if agent2.category == Condition.CURE:
        return [improve(agent1), agent2]

  
    return worsen_pair(agent1, agent2)
def meetup(agent_listing: tuple) -> list:
    agents = list(agent_listing)
    updated = []

  
    valid = [agent for agent in agents if agent.category not in {Condition.HEALTHY, Condition.DEAD}]
    untouched = [agent for agent in agents if agent.category in {Condition.HEALTHY, Condition.DEAD}]

    i = 0
    while i < len(valid):
        if i + 1 < len(valid):
            updated += resolve_meeting(valid[i], valid[i+1])
            i += 2
        else:
            updated.append(valid[i])  
            i += 1

    return updated + untouched