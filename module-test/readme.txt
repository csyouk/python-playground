참고
- https://docs.python.org/3/whatsnew/2.1.html#other-changes-and-fixes
- http://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
- http://www.gossamer-threads.com/lists/python/python/935504

Modules can now control which names are imported when from module import * is used,
by defining an __all__ attribute containing a list of names that will be imported.
One common complaint is that if the module imports other modules such as sys or string,
from module import * will add them to the importing module’s namespace.
To fix this, simply list the public names in __all__:

# List public names
__all__ = ['Database', 'open']

A stricter version of this patch was first suggested and implemented by Ben Wolfson,
but after some python-dev discussion, a weaker final version was checked in.

__all__ 이라고 된 곳에 객체들을 등록해 놓으면, 해당 모듈을 접근할 때, __all__에 등록된 객체들만
접근해서 쓸 수 있다.

java의 public과 비슷하다.

차이점이 있다면, 파이썬은 모듈단위로 설계하는 것을 권장하고, 해당 모듈에 최대한 함수 단위로 짜는 것을
권장한다.

java는 1 class = 1 java file 을 칼 같이 지킨다.
