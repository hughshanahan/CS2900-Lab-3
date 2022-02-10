test = {
    'name': 'checkpoint-7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # Hmm, can't find the Mnew variable. Check the name.
                    >>> # Have you defined it properly?
                    >>> "Mnew" in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your Mnew is wrong by at least 0.001.
                    >>> # Double check your u_hat vector.
                    >>> np.allclose(Mnew, np.load('tester/res/Mnew.npy'), atol=10**-3, rtol=0)
                    True
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
