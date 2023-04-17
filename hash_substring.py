# Python 3
B = 3
Q = 256
def read_input():
    choice = input().strip()
    if choice == 'F':
        with open('test_input.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = input().strip()
        text = input().strip()
    return pattern, text

def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    PRIME = 10**9+7
    BASE = 31
    p_len = len(pattern)
    t_len = len(text)

    # Calculate the hash of the pattern and the first substring of the same length in the text
    pattern_hash = 0
    text_hash = 0
    for i in range(p_len):
        pattern_hash = (pattern_hash * BASE + ord(pattern[i])) % PRIME
        text_hash = (text_hash * BASE + ord(text[i])) % PRIME

    # Calculate BASE^(p_len-1) for rolling hash computation
    power = 1
    for i in range(p_len-1):
        power = (power * BASE) % PRIME

    # Check each substring of length p_len of the text for a match with the pattern
    occurrences = []
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])

    for i in range(text_length - pattern_length + 1):
        if text_hash == pattern_hash:
            if text[i:i + pattern_length] == pattern:
                occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = (B*(text_hash-ord(text[i])*multiplier)+ord(text[i+pattern_length]))%Q
    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

   # Alens Ilgavižs 221RDB312 4.G 