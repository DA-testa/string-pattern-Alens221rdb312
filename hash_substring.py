# Python 3
B = 13
Q = 256
def read_input():
    choice = input().strip()
    if choice == 'F':
        with open('tests/06', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()
    return pattern, text

def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_hash(pattern) -> int:
    global B, Q
    length = len(pattern)
    result = 0
    for i in range(length):
        result = (B*result+ord(pattern[i]))%Q
    return result

def get_occurrences(pattern, text):
    global B, Q
    p_len = len(pattern)
    t_len = len(text)

    # Calculate BASE^(p_len-1) for rolling hash computation
    power = 1
    for i in range(p_len-1):
        power = (power * Q) % B

    # Check each substring of length p_len of the text for a match with the pattern
    occurrences = []
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:p_len])

    for i in range(t_len - p_len + 1):
        if text_hash == pattern_hash:
            if text[i:i + p_len] == pattern:
                occurrences.append(i)
        if i < t_len - p_len:
            text_hash = (B*(text_hash-ord(text[i])*power)+ord(text[i+p_len]))%Q
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

   # Alens Ilgavižs 221RDB312 4.G 