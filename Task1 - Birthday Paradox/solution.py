##
import numpy as np
import math
import random
from collections import defaultdict
import matplotlib.pyplot as plt


#####
# PLOTTING FUNCTION. DO NOT EDIT
plt_number = 1


def show_plt(name=None):
    if name == None:
        global plt_number
        name = "plot"+str(plt_number)
        plt_number = plt_number + 1
    filename = "cx_out/"+name
    plt.savefig(filename, bbox_inches="tight")
    print("A plot is available in the Files tab:", name)

#####

#####
# COMPUTE MATCH FUNCTION. DO NOT EDIT


def is_match(m: list, n: int = 2):
    """Returns True (if there are at least n repeated elements in the list) and False otherwise.
    Args:
        m (list): List of birthday dates
        n (int): Number of required element repetitions to count as a match.
                 Must be >0. Default: 2.
    Returns:
        bool
    """
    counter = defaultdict(int)
    for i in m:
        counter[i] += 1

    return max(counter.values()) >= n

#####


# First task: analytical approach
def analytical_prob(npeople: int, ndays: int):
    """ Compute analytical probability of at least 2 people having same birthday among 
    'npeople', assuming there are and 'ndays' in a year. This should match the formula you provided in Exercise 3.

    Args: 
    npeople <int>: Number of people 
    ndays <int>: Number of days in a year. Default: 365
    nrepeats <int>. Number of required element repetitions to count as a match. Default: 2. 

    Returns: 
    <float>:  Analytical probability
    """
    ###

    # TODO write your code here

    prob = 0.8956  # This is a placeholder. To be modified!

    n_perm_k = math.perm(ndays, npeople)
    total_perm = ndays**npeople
    p = n_perm_k/total_perm
    # Compute complementary
    prob = 1 - p

    ###

    return prob

# Second task: experiment simulation
def simulated_prob(npeople: int, ndays: int, nrepeats: int, ntrials: int = 200):
    """ Compute probability of at least 'nrepeats' people having same birthday among 
    'npeople', assuming there are 'ndays' in a year.

    Args: 
    npeople <int>: Number of people 
    nrepeats <int>: minimum number of people to share birthday to count as repetition
    ndays <int>: Number of days in a year. Default: 365
    ntrials <int>: Number of trials to run to estimate the probability. Default: 200

    Returns: 
    <float>:  Estimated probability using ntrials.
    """

    ####
    # TODO write your code here
    prob = 0.7879  # This is a placeholder. To be modified

    bths_range = range(1, ndays+1)
    matches = 0
    for _ in range(ntrials):
        # bths = [random.randint(1, ndays) for _ in range(npeople)]  # list of npeople random numbers sampled uniformly with replacement from [1, ndays] both included,
        # Alternatively:
        bths = random.choices(bths_range, k=npeople) # random.sample is without replacement

        imatch = is_match(bths, nrepeats)
        matches += imatch

    prob = matches / ntrials
    ####
    return prob

# Third task: Graph comparison
def graph_comparison(ndays: int, ntrials: int = 1000):
    """
    Plots analytical and simulated probability of a match as a function on npeople.

    Args:
        ndays (int): The number of possible days.
        ntrials (int, optional): The number of trials for the simulation. Default is 1000.

    """
    ####
    # TODO write your code here:
    #simulation
    # Return a list freq_sim of simulated probabilities,  where the ith element is the probability with (i+1)-th npeople people, npeople [1,100].
    # Your code here:
    
    ###
    freq_sim = []
    nrepeats = 2
    for npeople in range(1, 101):
        ratio = simulated_prob(npeople, ndays, nrepeats, ntrials)
        freq_sim.append(ratio)

    fig, ax = plt.subplots()
    ax.plot(freq_sim)
    ax.set_xlabel('Number of people')
    ax.set_ylabel('Probability of at least 2 matches')
    ax.set_title('Simulation approach')
    show_plt("simulation")

    ###
    # TODO write your code here:
    #analytical
    # Return a list freq_an of analytical probabilities, where the ith element is the probability with (i+1)-th npeople people, npeople [1,100]
    # Your code here:
    
    ###
    freq_an = []
    for npeople in range(1, 101):
        ratio = analytical_prob(npeople, ndays)
        freq_an.append(ratio)

    fig, ax = plt.subplots()
    ax.plot(freq_an)
    ax.set_xlabel('Number of people')
    ax.set_ylabel('Probability of at least 2 matches')
    ax.set_title('Analytical approach')
    show_plt("analytical")
