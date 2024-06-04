"""Example for a custom annotator."""

from sparv.api import Annotation, Output, annotator


@annotator("Convert every word to uppercase")
def uppercase(
    word: Annotation = Annotation("<token:word>"),
    out: Output = Output("<token>:sbx_uppercase.upper"),
    # some_config_variable: str = Config("sbx_uppercase.some_setting")
):
    """Convert to uppercase."""
    out.write([val.upper() for val in word.read()])

@annotator("Convert every word to lowercase")
def lowercase(
    word: Annotation = Annotation("<token:word>"),
    out: Output = Output("<token>:sbx_uppercase.lower"),
    # some_config_variable: str = Config("sbx_uppercase.some_setting")
):
    """Convert to lowercase."""
    out.write([val.lower() for val in word.read()])

@annotator("Count the number of nouns in a sentence")
def n_nouns_sentence(
    token_pos: Annotation = Annotation("<token:pos>"),
    sentence: Annotation = Annotation("<sentence>"),
    out: Output = Output("<sentence>:sbx_uppercase.nns"),
    # some_config_variable: str = Config("sbx_uppercase.some_setting")
):
    """Count the number of nouns."""
    sentences, orphans = sentence.get_children(token_pos)
    token_pos_list = list(token_pos.read())
    
    result = []
    for s in sentences:
        nncounter = 0
        #print(s)
        #print(nncounter)
        for i in s:
            if token_pos_list[i] == "NN":
                nncounter += 1
        result.append(str(nncounter))
    out.write(result)

@annotator("Count the number of nouns in a text")
def n_nouns_text(
    text: Annotation = Annotation("<text>"),
    sentence_nns: Annotation = Annotation("<sentence>:sbx_uppercase.nns"),
    out: Output = Output("<text>:sbx_uppercase.nnt"),
    # some_config_variable: str = Config("sbx_uppercase.some_setting")
):
    """Count the number of nouns."""
    texts, orphans = text.get_children(sentence_nns)
    print("texts", texts)
    sentence_nns_list = list(sentence_nns.read())
    print("sentence_nns_list", sentence_nns_list)

    result = []
    for t in texts:
        nncounter = 0
        for s in t:
            #print("sentence nn", s)
            nncounter += int(sentence_nns_list[s])
            #print("text nn", nncounter)
        result.append(str(nncounter))
    out.write(result)