# Simulating Language, Lab 2, Word learning
from numpy import prod 
import matplotlib.pyplot as plt

def normalize_probs(probs):
    """
    :probs: a list of numbers
    :returns: normalised list of numbers that sum to 1
    """
    total = sum(probs) #calculates the summed probabilities
    normedprobs = [(p/total) for p in probs] #normalise - divide by summed probs
    return normedprobs

# Terminology and example:
# hypothesis space (list): candidate word meanings (set) our learner considers, from which they can calculate each meaning's posterior probability
toy_hypothesis_space = [{0,1},{2}] # either it refers to entity 0 and entity 1, or it refers to entity 2
# labelling events (list): the entities that the word was referring to on a given labelling event

"""
Model assumptions:
- We'll assume there are 11 possible entities in the world, numbered 0 to 10.
- We'll assume that the word refers to between 1 and 6 entities (i.e. it doesn't \
refer to the empty set, it doesn't refer to everything).
- We'll assume that words refer to entities that are clustered in the space of possible \
entities, as represented by consecutive numbers. This is a bit arbitrary.
- We'll assume that all word meanings are equally likely. (Prior probability)
- We'll assume that words can only be used to label entities included in the word meaning \
(i.e. the word with meaning {0,1} can only be used to label entities 0 and 1, never entity 2, 3 etc)
- We'll assume that the word is equally likely to be used to label any entitity included in its \
meaning (i.e. the word with meaning {0, 1} is equally likely to be used to label entity 0 and entity 1; there is no priveledged meaning that it's most likely to be used for).
"""

def get_hypothesis_space(no_entities_in_world, no_poss_entities_per_meaning):
    all_entities = [i for i in range(0, no_entities_in_world)]
    

    all_hypotheses = []
    for i in range(0, len(all_entities)):
        for j in range(0, no_poss_entities_per_meaning):
            if i + j <= 10:
                all_hypotheses.append(set(range(i, i + j + 1)))

    all_hypotheses = sorted(all_hypotheses, key=lambda x: len(x))

    return all_hypotheses

def get_prior(possible_hypotheses):
    no_hypotheses = len(possible_hypotheses)
    prior = [1/no_hypotheses] * no_hypotheses
    return prior 


def get_likelihood(data, hypothesis):
    likelihoods = [1/len(hypothesis) if data_item in hypothesis else 0 for data_item in data]
    return prod(likelihoods)


def get_posterior_prob_dist(data, possible_hypotheses, prior):
    posteriors = []
    for i in range(len(possible_hypotheses)):
        h = possible_hypotheses[i]  
        prior_h = prior[i]  
        likelihood_h = get_likelihood(data, h) # calculate likelihood of data given this hypothesis
        posterior_h = prior_h * likelihood_h 
        posteriors.append(posterior_h) 
    return normalize_probs(posteriors) #finally, normalise to turn these numbers into a pr



all_hypotheses = get_hypothesis_space(11, 6)
prior = get_prior(all_hypotheses)
print(list(zip(all_hypotheses, get_posterior_prob_dist([0,0,1], all_hypotheses, prior))))