test = {
    'name': 'checkpoint-8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the P_3 variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "P_3" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your P_3 is wrong by at least 0.001.
                    >>> # This should just be a Numpy array containing both of the unit vectors.
                    >>> np.allclose(P_3, np.load('tester/res/P_3.npy'), atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Hmm, can't find the M_3 variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "M_3" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a 3x3 matrix here.
                    >>> # It seems like you're computing P . P^T instead of P^T . P
                    >>> # These should be the other way around. Convince yourself why.
                    >>> M_3.shape == (2, 2)
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # Your M_3 is wrong by at least 0.001.
                    >>> # Are you sure you're using the new variable P_3 and not P?
                    >>> np.allclose(M_3, np.load('tester/res/M_3.npy'), atol=10**-3, rtol=0)
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
