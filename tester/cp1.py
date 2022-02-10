test = {
    'name': 'checkpoint-1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems AB is undefined. Have you defined it correctly?
                    >>> 'AB' in dir()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Your multiplication is incorrect.
                    >>> # You must be using the matrices A and B as defined above.
                    >>> np.allclose(AB, np.array([[-1,2,1,11],[1,2,3,13]]), atol=10**-3, rtol=0)
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # This should throw an exception...
                    >>> # You seem to have redefined the value of A or B.
                    >>> np.matmul(B,A)
                    Traceback (most recent call last):
                    ...
                    ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 4)
                    """
                }
            ],
            'scored': True,
            'type': 'doctest'
        }
    ]
}
