test = {
    'name': 'checkpoint-4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems 'testSolutions' is undefined. Have you defined it correctly?
                    >>> # I.e. def testSolutions(C, d, y)
                    >>> "testSolutions" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your testSolutions function does not return a tuple!
                    >>> # You need to return something like (Boolean, ..., Boolean)
                    >>> isinstance(testSolutions(As, bs, solutions), tuple)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your testSolutions doesn't return the expected result.
                    >>> # Check you have chosen the correct matrices, vectors and solutions.
                    >>> testSolutions(As, bs, xs)
                    (False, False)
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
