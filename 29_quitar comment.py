def strip_comments(strng, markers):
    lines = strng.split('\n') # split input into lines
    print(lines)
    result_lines = []
    
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0] # keep part before marker
        result_lines.append(line.rstrip()) # remove trailing whitespace
    
    return '\n'.join(result_lines)
print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
# La función strip_comments elimina los comentarios de un string dado. 