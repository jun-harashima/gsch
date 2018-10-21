import unittest
from pyquery import PyQuery
from gsch.agent import Agent


class TestAgent(unittest.TestCase):

    def test__set_url_for(self):
        keywords = ['aaa', 'bbb']
        agent = Agent()
        url = agent._set_url_for(keywords)
        self.assertEqual(url, 'https://scholar.google.com/scholar?q=aaa+bbb')

    def test__extract_papers_from(self):
        html = """
        <html>
          <div class="gs_r gs_or gs_scl">
            <div class="gs_ggs gs_fl">
              <a href="https://smith2018.pdf"></a>
            </div>
            <div class="gs_ri">
              <h3><a>Awesome Study in 2018</a></h3>
              <div class="gs_a">John Smith - conference, 2018 - site_url</div>
              <div class="gs_rs">This paper introduces my awesome study.</div>
              <div class="gs_fl">Cited by 100</div>
            </div>
          </div>
        </html>
        """

        agent = Agent()
        pq_html = PyQuery(html)
        papers = agent._extract_papers_from(pq_html)
        self.assertEqual(papers[0].url, 'https://smith2018.pdf')
        self.assertEqual(papers[0].title, 'Awesome Study in 2018')
        self.assertEqual(papers[0].authors, ['John Smith'])
        self.assertEqual(papers[0].year, '2018')
        self.assertEqual(papers[0].cited_by, '100')
        self.assertEqual(papers[0].snippets,
                         'This paper introduces my awesome study.')


if __name__ == "__main__":
    unittest.main()
