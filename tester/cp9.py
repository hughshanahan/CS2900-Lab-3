test = {
    'name': 'checkpoint-9',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems 'X_3' is undefined. Have you defined it correctly?
                    >>> # I.e. X_3 = [np.array( . . . )]
                    >>> "X_3" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains too few or too many elements.
                    >>> # It should contain just the three vectors defined above.
                    >>> len(X_3)
                    3
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('X_3', X_3)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'Y_3' is undefined. Have you defined it correctly?
                    >>> # I.e. Y_3 = [np.array( . . . )]
                    >>> "Y_3" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains too few or too many elements.
                    >>> # It should contain just the four vectors defined above.
                    >>> len(Y_3)
                    3
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('Y_3', Y_3)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
