test = {
    'name': 'checkpoint-3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems 'checkNull' is undefined. Have you defined it correctly?
                    >>> # I.e. def checkNull(p)
                    >>> "checkNull" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your checkNull function isn't comparing the length properly.
                    >>> # Check the number of zeros you have specified.
                    >>> checkNull(np.array([10e-8,10e-8]))
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'Cs' is undefined. Have you defined it correctly?
                    >>> # I.e. Cs = [np.array( . . . ) ... ]
                    >>> "Cs" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'ds' is undefined. Have you defined it correctly?
                    >>> # I.e. ds = [np.array( . . . ) ... ]
                    >>> "ds" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'solutions' is undefined. Have you defined it correctly?
                    >>> # I.e. solutions = [np.array( . . . ) ... ]
                    >>> "solutions" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your solutions list is missing one or more solutions.
                    >>> # Check you have included all of valid solutions.
                    >>> [22.22222222222222, -22.22222222222222] in [ list(arr) for arr in solutions ]
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your solutions list is missing one or more solutions.
                    >>> # Check you have included all of valid solutions.
                    >>> [-1.3157894736842095, 10.526315789473685, 101.3157894736842] in [ list(arr) for arr in solutions ]
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
