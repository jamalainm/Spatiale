# coding: utf8
from __future__ import unicode_literals


# Stop words
STOP_WORDS = set(
    """
    ab ad an at atque aut

    cum

    de dum

    ea ego ei eo esse est et ex

    haec hanc hercle hic hinc hoc huc hunc

    iam id illam illi illum in is istuc ita

    me mi mihi modo

    nam ne neque nil non nos nunc

    o omnia

    pater

    quae quam que qui quid quidem quo quod quom

    re rem res

    scio se sed si sit sum sunt

    te tibi tu tum

    ubi ut uxorem
    """.split()
    )

contractions = ["'s"]
STOP_WORDS.update(contractions)

for apostrophe in ["‘", "’"]:
    for stopword in contractions:
        STOP_WORDS.add(stopword.replace("'", apostrophe))
