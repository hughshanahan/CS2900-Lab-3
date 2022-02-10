test = {
    'name': 'checkpoint-6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems 'X_cp6' is undefined. Have you defined it correctly?
                    >>> # I.e. X_cp6 = [np.array( . . . )]
                    >>> "X_cp6" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains too few or too many elements.
                    >>> # It should contain just the four matrices defined above.
                    >>> len(X_cp6)
                    4
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of matrices contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('X', X_cp6)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # It seems 'Y_cp6' is undefined. Have you defined it correctly?
                    >>> # I.e. Y_cp6 = [np.array( . . . )]
                    >>> "Y_cp6" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains too few or too many elements.
                    >>> # It should contain just the four matrices defined above.
                    >>> len(Y_cp6)
                    4
                    """
                },
                {
                    'code': r"""
                    >>> # Your list of vectors contains errors.
                    >>> # Check your definitions.
                    >>> from tester.utils import check_array_list
                    >>> check_array_list('Y', Y_cp6)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
