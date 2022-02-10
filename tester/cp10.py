test = {
    'name': 'checkpoint-10',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the M_3alt variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "M_3alt" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # We're expecting a 3x3 matrix here.
                    >>> # It seems like you're computing P . P^T instead of P^T . P
                    >>> # These should be the other way around. Convince yourself why.
                    >>> M_3alt.shape == (2, 2)
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # Your M_3alt is wrong by at least 0.001.
                    >>> # Are you sure you're using the correct unit vectors?
                    >>> np.allclose(M_3alt, np.load('tester/res/M_3alt.npy'), atol=10**-3, rtol=0)
                    True
                    """
                },
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
