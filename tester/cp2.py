test = {
    'name': 'checkpoint-2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems 'As' is undefined. Have you defined it correctly?
                    >>> # I.e. As = [np.array( . . . )]
                    >>> "As" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of matrices contains too few or too many elements.
                    >>> # It should contain just the four matrices defined above.
                    >>> len(As)
                    4
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of matrices contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('A', As)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'bs' is undefined. Have you defined it correctly?
                    >>> # I.e. bs = [np.array( . . . )]
                    >>> "bs" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains too few or too many elements.
                    >>> # It should contain just the four matrices defined above.
                    >>> len(bs)
                    4
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('b', bs)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
