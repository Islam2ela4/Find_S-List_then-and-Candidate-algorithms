                                                    Find-S Algorithm
FIND-S Algorithm starts from the most specific hypothesis and
generalize it by considering only positive examples.
• FIND-S algorithm ignores negative examples.
– As long as the hypothesis space contains a hypothesis that describes the true target concept,
and the training data contains no errors, ignoring negative examples does not cause to any
problem.
• FIND-S algorithm finds the most specific hypothesis within H that is
consistent with the positive training examples.
– The final hypothesis will also be consistent with negative examples if the correct target
concept is in H, and the training examples are correct.

1. Initialize h to the most specific hypothesis in H

2. For each positive training instance x

For each attribute constraint a, in h

If the constraint a, is satisfied by x

Then do nothing

Else replace a, in h by the next more general constraint that is

satisfied by x

3. Output hypothesis h


                                                  List-Then-Eliminate Algorithm
• List-Then-Eliminate algorithm initializes the version space to contain all
hypotheses in H, then eliminates any hypothesis found inconsistent with
any training example.

• The version space of candidate hypotheses thus shrinks as more
examples are observed, until ideally just one hypothesis remains that is
consistent with all the observed examples.

– Presumably, this is the desired target concept.

– If insufficient data is available to narrow the version space to a single hypothesis, then the
algorithm can output the entire set of hypotheses consistent with the observed data.

• List-Then-Eliminate algorithm can be applied whenever the hypothesis
space H is finite.

– It has many advantages, including the fact that it is guaranteed to output all hypotheses
consistent with the training data.

– Unfortunately, it requires exhaustively enumerating all hypotheses in H - an unrealistic
requirement for all but the most trivial hypothesis spaces.

1- $VersionSpace \leftarrow$ a list containing every hypothesis in $H$

2- For each training example, $\langle x, c(x) \rangle$

remove from $VersionSpace$ any hypothesis $h$ for which $h(x) \neq c(x)$

3- Output the list of hypotheses in $VersionSpace$

It requires exhaustively enumeration of all hypothesis in $H$ (huge!).

                                                Candidate-Elimination Algorithm
• The Candidate-Elimination algorithm computes the version space containing all
hypotheses from H that are consistent with an observed sequence of training examples.

• It begins by initializing the version space to the set of all hypotheses in H; that is, by
initializing the G boundary set to contain the most general hypothesis in H
G0  { <?, ?, ?, ?, ?, ?> }

and initializing the S boundary set to contain the most specific hypothesis
S0  { <0, 0, 0, 0, 0, 0> }

• These two boundary sets delimit the entire hypothesis space, because every other
hypothesis in H is both more general than S0 and more specific than G0.

• As each training example is considered, the S and G boundary sets are generalized and
specialized, respectively, to eliminate from the version space any hypotheses found
inconsistent with the new training example. 

• After all examples have been processed, the computed version space contains all the
hypotheses consistent with these examples and only these hypotheses.


• Initialize G to the set of maximally general hypotheses in H

• Initialize S to the set of maximally specific hypotheses in H

• For each training example d, do

– If d is a positive example

• Remove from G any hypothesis inconsistent with d ,

• For each hypothesis s in S that is not consistent with d ,-

– Remove s from S

– Add to S all minimal generalizations h of s such that

» h is consistent with d, and some member of G is more general than h

– Remove from S any hypothesis that is more general than another hypothesis in S

– If d is a negative example

• Remove from S any hypothesis inconsistent with d

• For each hypothesis g in G that is not consistent with d

– Remove g from G

– Add to G all minimal specializations h of g such that

» h is consistent with d, and some member of S is more specific than h

– Remove from G any hypothesis that is less general than another hypothesis in G


