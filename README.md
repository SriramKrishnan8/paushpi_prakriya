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
python3 -m tests.test.py -t "iw"
```

To test the working of iw\_saFJFA.py with own examples
```
python3 -m tests.test.py -t "iw" -o "dukqF"
```

### Testing (prawyAhAra)

To test the working of prawyAhAra\_saFjFA.py with default examples
```
python3 -m tests.test.py -t "prawyAhAra"
```

To test the working of prawyAhAra\_saFjFA.py with own examples
```
python3 -m tests.test.py -t "prawyAhAra" -o "ac"
```

### Testing (ti)

To test the working of ti with default examples
```
python3 -m tests.test.py -t "ti"
```

To test the working of ti with own examples
```
python3 -m tests.test.py -t "ti" -o "gamLz"
```

### Testing (upaXA)

To test the working of upaXA with default examples
```
python3 -m tests.test.py -t "upaXA"
```

To test the working of upaXA with own examples
```
python3 -m tests.test.py -t "ti" -o "dupacazR"
```


### Testing (XAwu operations)

This involves handling the "iw" variable followed by the satva, ṇatva, numāgama and upadhādīrgha operations on the dhātu

To test the working of upaXA with default examples
```
python3 -m tests.test.py -t "XAwu_changes"
```

To test the working of upaXA with own examples
```
python3 -m tests.test.py -t "XAwu_changes" -o "dupacazR"
```


