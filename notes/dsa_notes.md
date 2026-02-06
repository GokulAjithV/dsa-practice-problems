
# 32 and 64 bits integers - signed and unsigned
## What are Bits?

A **bit** is the smallest unit of data in computing - it can be either 0 or 1. When we talk about a 32-bit or 64-bit integer, we're talking about how many bits are used to store that number in memory. [stackoverflow](https://stackoverflow.com/questions/5812406/16-bit-int-vs-32-bit-int-vs-64-bit-int)

## 32-bit vs 64-bit Integers

**32-bit integer**: Uses 32 bits (32 zeros and ones) to represent a number [stackoverflow](https://stackoverflow.com/questions/5812406/16-bit-int-vs-32-bit-int-vs-64-bit-int)
- Can represent 2^32 different values (about 4.29 billion different numbers) [stackoverflow](https://stackoverflow.com/questions/5812406/16-bit-int-vs-32-bit-int-vs-64-bit-int)
- Range: -2,147,483,648 to 2,147,483,647 for signed integers [educative](https://www.educative.io/answers/int-32-vs-int-64-in-cpp)
- Memory: Takes 4 bytes of space [educative](https://www.educative.io/answers/int-32-vs-int-64-in-cpp)

**64-bit integer**: Uses 64 bits to represent a number [stackoverflow](https://stackoverflow.com/questions/5812406/16-bit-int-vs-32-bit-int-vs-64-bit-int)
- Can represent 2^64 different values (about 18 quintillion different numbers) [geeksforgeeks](https://www.geeksforgeeks.org/operating-systems/32-bit-vs-64-bit-operating-systems/)
- Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 for signed integers [educative](https://www.educative.io/answers/int-32-vs-int-64-in-cpp)
- Memory: Takes 8 bytes of space [educative](https://www.educative.io/answers/int-32-vs-int-64-in-cpp)

**Why it matters for your problem**: The LeetCode problem specifies a 32-bit signed integer constraint. This means if your reversed number goes beyond -2,147,483,648 or above 2,147,483,647, you need to return 0 (handle overflow).

## Signed vs Unsigned Integers

This is about whether the integer can be negative or not.

**Signed integers**: Can be both positive AND negative
- Uses one bit (the leftmost bit) to represent the sign (+ or -)
- For 32-bit signed: Range is -2,147,483,648 to 2,147,483,647
- This is the default in most programming languages (like Python's int, Java's int)

**Unsigned integers**: Can only be positive (zero or greater)
- All bits are used for the magnitude (no sign bit needed)
- For 32-bit unsigned: Range is 0 to 4,294,967,295 (double the positive range!)
- Used when you know a value will never be negative (like array sizes, counts)
