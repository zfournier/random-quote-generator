from random_quote_generator import get_quote
from random_quote_generator.quotes import quotes


def test_get_quote():
    """
    GIVEN
    When get_quote is called
    Then random quote is returned
    """
    quote = get_quote()

    assert quote in quotes
