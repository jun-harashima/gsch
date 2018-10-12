class Paper:

    def __init__(self, title, authors=[], year=None, cited_by=None, url=None,
                 snippets=[]):
        self.title = title
        self.authors = authors
        self.year = year
        self.cited_by = cited_by
        self.url = url
        self.snippets = snippets
