import textacy


def load_doc(text):
    return textacy.Doc(textacy.preprocess.normalize_whitespace(text).replace('’', '\''), metadata=None)


def extract_keywords(textacy_doc, number=10):
    return textacy.keyterms.textrank(textacy_doc, normalize=None, n_keyterms=number)


def extract_keyphrases(textacy_doc, number=10):
    return textacy.keyterms.sgrank(textacy_doc, ngrams=(1, 2, 3, 4, 5, 6), normalize=None, window_width=1500, n_keyterms=number, idf=None)


def extract_unique_named_entities(textacy_doc):
    lis = textacy.extract.named_entities(textacy_doc, drop_determiners=True, exclude_types='numeric')
    clean_lis = []
    [clean_lis.append(x.text) for x in lis if x.text not in clean_lis]
    return clean_lis


def filter_keywords(keywords_span):
    return map(lambda x: x[0], keywords_span)


def filter_keyphrases(keyphrases_span):
    return map(lambda x: x[0], keyphrases_span)


def get_keywords_list(text, number=10):
    return list(filter_keywords(extract_keywords(load_doc(text), number)))


def get_keyphrases_list(text, number=10):
    return list(filter_keyphrases(extract_keyphrases(load_doc(text), number)))


def get_named_entities(text, number=10):
    return extract_unique_named_entities(load_doc(text))[:number]

