====
gsch
====

.. image:: https://img.shields.io/pypi/v/gsch.svg
    :target: https://pypi.python.org/pypi/gsch

.. image:: https://img.shields.io/travis/jun-harashima/gsch.svg
    :target: https://travis-ci.org/jun-harashima/gsch

gsch is a tool for handling paper information in a Google Scholar results page.

Quick Start
===========

To install gsch, run this command in your terminal:

.. code-block:: bash

   $ pip install gsch

Using gsch, you can handle paper information in a Google Scholar results page as follows:

.. code-block:: python

   from gsch.agent import Agent
   from gsch.paper import Paper

   agent = Agent()
   papers = agent.search(['some', 'topic'])

For a given query, ``agent`` obtains 10 search results on Google Scholar. Please be careful not to send too many requests to the service because there is a query limit.

``agent`` organizes the search results into the ``Paper`` instances, each of which consists of the following attributes:

- title
- authors
- year
- cited_by
- url
- snippets

You will often obtain better results as follows:

.. code-block:: python

   agent = Agent()
   option = Option(year_low=2017)
   papers = agent.search(['some', 'topic'], option)

In this case, ``papers`` consists of papers that have been published since 2017. Like this, you can use the following options:

- ``year_low``: if you set ``year_low=2017``, you obtain papers that have been published since 2017
- ``year_high``: if you set ``year_high=2017``, you obtain papers that have been published by 2017
- ``start``: if you set ``start=10``, you obtain papers that are ranked from 11 to 20
