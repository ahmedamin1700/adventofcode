import re

with open('day-3/input.txt', 'r') as file:
    lines = file.readlines()

text = ""

for line in lines:
    text += line.strip()

text_ = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

token_regex = re.compile(
    r"(?P<MUL>mul[(](\d{1,3}),(\d{1,3})[)])"
    r"|(?P<DONOT>don't\(\))"
    r"|(?P<DO>do\(\))" 
)

tokens = token_regex.finditer(text)

should_process_mul = True 
results = 0

for match in tokens:
    token_type = match.lastgroup
    
    if token_type == 'DONOT':
        should_process_mul = False
    
    elif token_type == 'DO':
        should_process_mul = True
        
    elif token_type == 'MUL':
        pair = match.group(2, 3)
        if should_process_mul:
            try:
                num1 = int(pair[0])
                num2 = int(pair[1])
                results += (num1 * num2)
            except ValueError:
                print(f"   (Skipping non-integer pair: {pair})")
        else:
            print(f"-> Skipping disabled MUL: {pair}")

print("\nFinal Multiplication Results:", results)