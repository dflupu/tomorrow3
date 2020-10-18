# tomorrow3

This is an implementation of the [tomorrow](https://github.com/madisonmay/tomorrow) package that supports python >= 3.0

Notable differences:
- Calls made when when all of the threads are occupied result in the call blocking instead of returning immediately
- Added a .wait() method on the decorated function that waits until all of the tasks complete
- Exceptions are rethrown on the main thread on subsequent calls or on .wait()
