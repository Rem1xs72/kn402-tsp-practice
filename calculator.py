from numbers import Real

def add(a: Real, b: Real) -> Real:
    """Додає два числа. Рядки та логічні значення відхиляє."""
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, Real) or not isinstance(b, Real):
        raise TypeError('Arguments must be real numbers')
    return a + b

if __name__ == '__main__':
    print('Result:', add(2, 3))
