NUM_WORD = {90: "ninety", 80: "eighty", 70: "seventy", 60: "sixty", 50: "fifty",
            40: "fourty", 30: "thirty", 20: "twenty", 19: "nineteen", 18: "eighteen",
            17: "seventeen", 16: "sixteen", 15: "fifteen", 14: "fourteen", 13: "thirteen",
            12: "twelve", 11: "eleven", 10: "ten", 9: "nine", 8: "eight", 7: "seven",
            6: "six",  5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}


def text_numeral(num: int) -> str:
    """

    This functions takes in a positive integer below 100 and returns a string
    representing the number in text form.

    Parameters
    ----------
    num: int
        Number to be converted to text

    Returns
    -------
    str
        Number in text form

    Examples
    --------
    >>> text_numeral(15)
    'fifteen'
    >>> text_numeral(29)
    'twenty nine'
    """
    word = ''
    for key, value in NUM_WORD.items():
        if num >= key:
          num -= key
          word += value + ' '
        if num == 0:
          break
          
    word = word.strip()
    return word