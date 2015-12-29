# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are very similar in the way that they store a bunch of values and organize them in a numbered index starting from zero. <br>
The main difference is that a list is mutable which means that its values can be changed. <br>
```
mytuple = (1,2,3)
mytuple[2] = 4
```
```
TypeError                    Traceback (most recent call last)
<ipython-input-6-37ac2a87abf7> in <module>()
      1 a = (1,2,3)
----> 2 a[2] = 4
TypeError: 'tuple' object does not support item assignment
```
<br>
The keys of a dictionnary must be immutable. Thus only tuples will work as keys in dictionnaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> |        List       |         Set         |
|:-----------------:|:-------------------:|
|    Keeps order    |  Doesn't keep order |
|    Every types of  items    | Only hashable items |
| Allows duplicates |  Forbids duplicates |
<br>
When it comes to checking if an element is in the given structure, sets are much faster than list. Indeed, they are implemented using hash tables in which the time complexity of finding an element is O(1) (constant time) while it is O(n) for a list (proportional to its size).
<br>
```
l = [1, 3, 4, 8, 3, 1, 12, 4]
s = set(l)
print l
print s
```
```
[1, 3, 4, 8, 3, 1, 12, 4]
{1, 3, 4, 8}
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a simple way in Python to construct throaway functions. <br>
For instance, to sort a list of people by age:
```
people_list = [
("thomas", 24, "French", "M"),
("lisa", 22, "German", "F"),
("andrew", 25, "English", "M")
         ]
sorted (people_list, key=lambda people: people[1])
```
```
[('lisa', 22, 'German', 'F'),
 ('thomas', 24, 'French', 'M'),
 ('andrew', 25, 'English', 'M')]
 ```


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a concpt that is used to construct list in a very natural and simple way instead of using `for`and `if`statements.<br>
See `05a-python/Q4.ipynb` for the examples.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.
a.

```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```

>> 937

b.
```
date_start = '12312013'
date_stop = '05282015'
```

>> 513

c.
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)
>>
```
7 items passed all tests:
   4 tests in q6_strings.both_ends
   4 tests in q6_strings.donuts
   4 tests in q6_strings.fix_start
   3 tests in q6_strings.front_back
   4 tests in q6_strings.mix_up
   4 tests in q6_strings.not_bad
   3 tests in q6_strings.verbing
26 tests in 8 items.
26 passed and 0 failed.
Test passed.
```
---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)
>>
```
5 items passed all tests:
   3 tests in q7_lists.front_x
   3 tests in q7_lists.linear_merge
   3 tests in q7_lists.match_ends
   4 tests in q7_lists.remove_adjacent
   3 tests in q7_lists.sort_last
16 tests in 6 items.
16 passed and 0 failed.
Test passed.
```


---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





