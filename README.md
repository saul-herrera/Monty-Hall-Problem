# Monty-Hall-Problem
A simulation of the Monty Hall Problem that verifies its counterintuitive solution.

The Monty Hall problem:
>"Suppose you're on a game show, and you're given the choice of three doors:
>Behind one door is a car; behind the others, goats. You pick a door, say No. 1,
>and the host, who knows what's behind the doors, opens another door, say No. 3, 
>which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it 
>to your advantage to switch your choice?"
>(from [Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)).

So any one of the three doors could have the car, which means you would have a 1/3 probability of winning. One may think: "how could switching my choice make any difference on my chances of winning?".

This problem is famous for having a non-intuitive solution. It turns out switching doors doubles your probability of winning: you have a 2/3 probability of winning if you switch, compared to 1/3 if you don't. 

After knowing the correct answer, you might try to convince yourself that this makes sense, but it doesn't. According to [some accounts](https://web.archive.org/web/20140413131827/http://www.decisionsciences.org/DecisionLine/Vol30/30_1/vazs30_1.pdf), not even Paul Erdős, the famous mathematician, was fully convinced of this result until he was shown a Monte Carlo simulation of the problem (allegedly, he objected that he still didn't understand it, but at least now he was convinced it was true).

This example attempts to ilustrate that a computer program can be used to find correct answers to problems that are difficult to grasp by pure reasoning.
