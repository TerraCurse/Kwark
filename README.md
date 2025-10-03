# Kwark
A brainfuck-esque programming language, with an interpreter written in python.
# Basics
In kwark, you only have 4 "bits".
Bits can be used to store values, like in brainfuck.
The maximum value of a bit can be 94, as that is the amount of supported characters in kwark.
So for example, a bit with the value of 10 would output an "A" (uppercase).
If the value of the bit your trying to increment exceeds 94, it will be reset to 0.
If the value of the bit your trying to decrement goes below 0, it will be reset to 94.
## Keywords (of sorts)
* i - Increments the value of the current bit by 1.
* I - Increments the value of the current bit by 2.
* d - Decrements the value of the current bit by 1.
* D - Decrements the value of the current bit by 2.
* n - Switches to the next bit. (switches to 0 if you try to switch to bit 5)
* p - Switches to the previous bit. (switches to 4 if you try to switch to bit -1.)
* o - Outputs the character corresponding to the bit value. (0 = 0, 10 = A, 27 = a)
