# Valid variable names
first_name = "John"  # snake_case (recommended for variables)
age2 = 22  # letters + numbers (number not at start)
TOTAL = 100  # UPPERCASE (recommended for constants)
_private = "hidden"  # starts with underscore (private-ish variable)
__dunder__ = "special"  # double underscore (special/magic variables)
user_name_1 = "Alice"  # multiple underscores and numbers
lastName = "Smith"  # camelCase (works but not Pythonic)
data123 = [1, 2, 3]  # ends with numbers
_internal_var = 42  # single leading underscore
MAX_SPEED = 120  # constant with underscore

print(first_name)
print(age2)
print(TOTAL)

# Invalid variable name examples (left commented to avoid syntax errors):
# 2age = 20                  # starts with number
# first-name = "Doe"         # hyphens not allowed (use underscore)
# my variable = 50           # spaces not allowed
# class = "Math"             # reserved keyword (use class_ instead)
# for = 10                   # reserved keyword
# def = "test"               # reserved keyword
# user@name = "test"         # special characters not allowed
# first.name = "John"        # dots not allowed
# user#1 = "test"            # # symbol not allowed
# 123abc = 100               # starts with number

# Valid but not recommended (ambiguous or vague names)
ell_var = 10  # avoid single-letter names like l (looks like 1)
oh_var = 20  # avoid names that look like 0
eye_var = 30  # avoid names that look like l or 1
x = "data"  # not descriptive (use meaningful names)
temp = 42  # vague name (temp for what?)
a = b = c = 100  # multiple assignment (use sparingly)
