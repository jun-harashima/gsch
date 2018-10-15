# gsch

[![](https://img.shields.io/pypi/v/gsch.svg)](https://pypi.python.org/pypi/gsch) [![](https://img.shields.io/travis/jun-harashima/gsch.svg)](https://travis-ci.org/jun-harashima/gsch)

gsch is a tool for handling paper information in a Google Scholar results page.

## Quick Start

To install gsch, run this command in your terminal:

```
$ pip install gsch
```

You can handle paper information in a Google Scholar results page like this:

```
from gsch.agent import Agent
from gsch.paper import Paper

agent = Agent()
papers = agent.search(['some', 'topic'])
```

For a given query, gsch obtains 10 search results on Google Scholar and organizes them into `Paper` instances. Each of the instance consists of the following attributes:

- title
- authors
- year
- cited_by
- url
- snippets

Please be careful not to send too many requests to Google Scholar because there is a query limit.
