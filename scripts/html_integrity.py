"""Catch literal comparisons accidentally parsed as tags before card content disappears.

Element names checked against the HTML, SVG 2 and MathML 3 element indexes:
https://html.spec.whatwg.org/multipage/indices.html#elements-3
https://www.w3.org/TR/SVG2/eltindex.html
https://www.w3.org/TR/MathML3/appendixi.html
This is a content-loss guard, not a complete HTML conformance or rendering check.
"""
from html.parser import HTMLParser

HTML_TAGS = set("""
a abbr address area article aside audio b base bdi bdo blockquote body br button canvas caption cite code col
colgroup data datalist dd del details dfn dialog div dl dt em embed fieldset figcaption figure footer form h1
h2 h3 h4 h5 h6 head header hgroup hr html i iframe img input ins kbd label legend li link main map mark menu
meta meter nav noscript object ol optgroup option output p picture pre progress q rp rt ruby s samp script
search section select selectedcontent slot small source span strong style sub summary sup table tbody td
template textarea tfoot th thead time title tr track u ul var video wbr
""".split())
SVG_TAGS = set("""
a animate animatemotion animatetransform circle clippath defs desc discard ellipse feblend fecolormatrix
fecomponenttransfer fecomposite feconvolvematrix fediffuselighting fedisplacementmap fedistantlight
fedropshadow feflood fefunca fefuncb fefuncg fefuncr fegaussianblur feimage femerge femergenode femorphology
feoffset fepointlight fespecularlighting fespotlight fetile feturbulence filter foreignobject g image line
lineargradient marker mask metadata mpath path pattern polygon polyline radialgradient rect set stop style svg
switch symbol text textpath title tspan use view
""".split())
MATHML_TAGS = set("""
abs and annotation annotation-xml apply approx arccos arccosh arccot arccoth arccsc arccsch arcsec arcsech
arcsin arcsinh arctan arctanh arg bind bvar card cartesianproduct cbytes ceiling cerror ci cn codomain
complexes compose condition conjugate cos cosh cot coth cs csc csch csymbol curl declare degree determinant
diff divergence divide domain domainofapplication emptyset eq equivalent eulergamma exists exp exponentiale
factorial factorof false floor fn forall gcd geq grad gt ident image imaginary imaginaryi implies in infinity
int integers intersect interval inverse lambda laplacian lcm leq limit list ln log logbase lowlimit lt maction
maligngroup malignmark math matrix matrixrow max mean median menclose merror mfenced mfrac mglyph mi min minus
mlabeledtr mlongdiv mmultiscripts mn mo mode moment momentabout mover mpadded mphantom mprescripts mroot mrow
ms mscarries mscarry msgroup msline mspace msqrt msrow mstack mstyle msub msubsup msup mtable mtd mtext mtr
munder munderover naturalnumbers neq none not notanumber notin notprsubset notsubset or otherwise outerproduct
partialdiff pi piece piecewise plus power primes product prsubset quotient rationals real reals reln rem root
scalarproduct sdev sec sech selector semantics sep set setdiff share sin sinh span subset sum tan tanh tendsto
times transpose true union uplimit variance vector vectorproduct xor
""".split())

STANDARD_TAGS = HTML_TAGS | SVG_TAGS | MATHML_TAGS

# HTML permits these omitted end tags; do not turn this guard into a strict XML parser.
VOID_TAGS = set("area base br col embed hr img input link meta source track wbr".split())
OPTIONAL_END_TAGS = set("html head body p li dt dd rb rt rp rtc optgroup option colgroup thead tbody tfoot tr td th".split())

class MarkupIntegrity(HTMLParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.required_closings = []

    def check_tag(self, tag):
        assert tag in STANDARD_TAGS, (
            f"Unexpected HTML/SVG/MathML tag <{tag}>; a literal comparison may swallow teaching text. "
            "Escape text '<' as '&lt;' (or use MathML). Check a genuine new element before extending support."
        )

    def check_start_token(self):
        # A swallowed sentence can collide with genuine tags such as <s> or <q>.
        # HTMLParser then consumes the later </p> as part of a permissive start tag.
        quote = None
        for char in self.get_starttag_text()[1:]:
            if quote:
                if char == quote:
                    quote = None
            elif char in ("'", '"'):
                quote = char
            elif char == '<':
                raise AssertionError("Unquoted '<' inside a start tag may swallow teaching text. Escape text '<' as '&lt;' (or use MathML).")

    def handle_starttag(self, tag, attrs):
        self.check_tag(tag)
        self.check_start_token()
        if tag not in VOID_TAGS | OPTIONAL_END_TAGS:
            self.required_closings.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.check_tag(tag)
        self.check_start_token()

    def handle_endtag(self, tag):
        self.check_tag(tag)
        if tag in VOID_TAGS | OPTIONAL_END_TAGS:
            return
        assert self.required_closings and self.required_closings[-1] == tag, (
            f"Unmatched or misnested </{tag}> may hide teaching text. Check paired tags; escape text '<' as '&lt;'."
        )
        self.required_closings.pop()

    def close(self):
        super().close()
        assert not self.required_closings, (
            f"Unclosed <{self.required_closings[-1]}> may be a swallowed comparison. Escape text '<' as '&lt;' or close the real element."
        )


def validate_markup(markup):
    parser = MarkupIntegrity(convert_charrefs=True)
    parser.feed(markup)
    parser.close()
