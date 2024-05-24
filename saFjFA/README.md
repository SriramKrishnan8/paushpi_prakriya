# Implementation of iw and prawyAhAra saFjFA

The following are the constituents:
1. iw\_saFjFA.py - contains the functions for each of the sUwras that define an iw saFjFA along with the elision function (wasya\_lopaH).
2. prawyAhAra\_saFjFA.py - contains the functions to generate the letters corresponding to the given prawyAhAra
2. util.py - contains various lists like ac, hal, XAwus, prawyayas, etc.
3. test.py - default examples for testing are given. We can also provide our own example.

## Testing (iw)

To test the working of iw\_saFJFA.py with default examples
```
python3 test.py -t "iw"
```

To test the working of iw\_saFJFA.py with own examples
```
python3 test.py -t "iw" -o "dukqF"
```

## Testing (prawyAhAra)

To test the working of prawyAhAra\_saFjFA.py with default examples
```
python3 test.py -t "prawyAhAra"
```

To test the working of prawyAhAra\_saFjFA.py with own examples
```
python3 test.py -t "prawyAhAra" -o "ac"
```


## To be done

The iw module works for a sample set of XAwus and prawyayas. The following are to be updated:
1. List of all XAwus should be stored in the util.py file. At present, there are only a few XAwus.
2. List of all prawyayas are to be enlisted in the util.py file. Additionally, viBakwi\_prawyayas and taxXiwa\_prawyayas are to be maintained separately.
3. For "upaxeSa", all the XAwus, prawyayas, Agamas, AxeSas and terms used in the sUwrapATa are to be enlisted.

The prawyAhAra module works for all prawyAhAras. Additionally it also produces the xIrGa forms of the vowels. Should check if the xIrGa of all consonants are also to be produced. And also whether pluwa is required or not.
