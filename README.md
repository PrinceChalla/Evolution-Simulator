Evolution Simulator

This is an evolution simulator built using Python and Pygame. The simulator models the interactions between three classes of entities: trees, carnivores, and herbivores. The animals in the simulation have various traits and evolve over time based on random mutations and interactions.
Features

    Animals: There are two types of animals in the simulation — Carnivores and Herbivores. Each animal has the following traits:
        Speed: Determines how fast the animal moves.
        Lifespan: How long the animal lives before dying.
        Mutation Chance: Probability of an animal undergoing a mutation each time it reproduces.
        Fertility: The animal's ability to reproduce.
        Size: The size of the animal, affecting its ability to move and interact with other animals.
        Color: Each animal has a unique color.

    Rule: Carnivores cannot eat herbivores that have the same color. This introduces an additional layer of strategy and evolution to the simulation.

    Trees: Trees populate the environment, providing resources (like food) for the herbivores.

How it works

    Evolution: Animals evolve over time through mutation. Their traits can change randomly based on their mutation chance, which influences how they adapt to their environment.
    Carnivores and Herbivores Interaction: Herbivores roam the environment, eating trees, while carnivores hunt herbivores. However, carnivores cannot eat herbivores of the same color.
    Reproduction: Animals with higher fertility will reproduce more often, passing their traits (including mutations) to the next generation.

Installation

    Clone this repository:

git clone https://github.com/PrinceChalla/Evolution-Simulator.git
cd Evolution-Simulator

Install dependencies:

    pip install pygame

Usage

To run the simulation, simply run the simulation.py script:

python simulation.py

Contributing

Feel free to open issues or submit pull requests to improve the simulation! If you have ideas for new features, don't hesitate to suggest them.
