# Paushpi Prakriya

Mechanical implementation of the Paushpi Prakriya. This package contains scripts that perform various tasks from Aṣṭādhyāyī. It completely follows the Paushpi Prakriya. This is in the initial stages of development. The entire project functions in WX notation.

## Requirements

```
python, bash
```


## Clone the project:

Run in terminal:

```
git clone https://github.com/SriramKrishnan8/paushpi_prakriya
```

## Testing

```
cd paushpi_prakriya/
```

### Testing (iw)

To test the working of iw\_saFJFA.py with default examples
```
python3 -m tests.test -t "iw"
```

To test the working of iw\_saFJFA.py with own examples
```
python3 -m tests.test -t "iw" -o "dukqF"
```

### Testing (prawyAhAra)

To test the working of prawyAhAra\_saFjFA.py with default examples
```
python3 -m tests.test -t "prawyAhAra"
```

To test the working of prawyAhAra\_saFjFA.py with own examples
```
python3 -m tests.test -t "prawyAhAra" -o "ac"
```

### Testing (ti)

To test the working of ti with default examples
```
python3 -m tests.test -t "ti"
```

To test the working of ti with own examples
```
python3 -m tests.test -t "ti" -o "gamLz"
```

### Testing (upaXA)

To test the working of upaXA with default examples
```
python3 -m tests.test -t "upaXA"
```

To test the working of upaXA with own examples
```
python3 -m tests.test -t "ti" -o "dupacazR"
```

### Testing (XAwu operations)

This involves handling the "iw" variable followed by the satva, ṇatva, numāgama and upadhādīrgha operations on the dhātu

To test the working of XAwu operations with default examples
```
python3 -m tests.test -t "XAwu_changes"
```

To test the working of XAwu operations with own examples
```
python3 -m tests.test -t "XAwu_changes" -o "dupacazR"
```


### Testing (vikaraNa)

This involves inserting the "vikaraNa-prawyaya" based on whether the "wif-prawyaya" is sārvadhātuka or ārdhadhātuka, whether the prayoga is kartṛvācya, karmavācya or bhāvavācya and the gaṇa of the give dhātu.

At present we have a set of examples where we provide all the necessary information and then insert the vikaraṇa accordingly. To test it:
```
python3 -m tests.test -t "vikaraNa"
```

### Testing (prakriyA)

A sample prakriyA format is created and can be tested on some given examples in tests/test.py. To test it:
```
python3 -m tests.test -t "prakriyA"
```

As of now, the options are fixed in the examples. Soon, provision for users to provide their own examples will be added.