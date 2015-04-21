from sphinx.writers import html as sphinx_htmlwriter

class LettuceHTMLTranslator(sphinx_htmlwriter.SmartyPantsHTMLTranslator):
    """
    Lettuce-customized HTML transformations of documentation. Based on
    djangodocs.DjangoHTMLTranslator
    """

    def visit_section(self, node):
        node['ids'] = ["lettuce-%s" % x for x in node['ids']]
        sphinx_htmlwriter.SmartyPantsHTMLTranslator.visit_section(self, node)
