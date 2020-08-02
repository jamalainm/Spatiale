# Spatiale

A developing model of Latin language

# Lemmatization

* Added lookup list to <.env/lib/python3.7/site-packages/spacy_lookups_data/data/>
* Edited <.env/lib/python3.7/site-packages/spacy_lookups/__init__.py> and added the following to the end of the file
	* <la = {"lemma_lookup": get_file("la_lemma_lookup.json")}>
* Edited <setup.cfg> under <lookups> and added:
	* <la = spacy_lookups_data:la>
