def strip_comments(strng, markers):
    lines = strng.split('\n') # split input into lines
    print(lines)
    result_lines = []
    
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
        result_lines.append(line.rstrip())
    
    return '\n'.join(result_lines)
print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))