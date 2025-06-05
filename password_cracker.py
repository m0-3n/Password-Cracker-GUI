import random
import time
import string

class CrackerState:
    stop = False

def get_adaptive_charset(password):
    charset = set()
    
    if any(c.islower() for c in password):
        charset.update(string.ascii_lowercase)
    if any(c.isupper() for c in password):
        charset.update(string.ascii_uppercase)
    if any(c.isdigit() for c in password):
        charset.update(string.digits)
    if any(c in string.punctuation for c in password):
        charset.update(string.punctuation)
        
    return ''.join(charset)

def brute_force(password, state: CrackerState):
    charset = get_adaptive_charset(password)
    attempts = 0
    start = time.time()
    guess = ""

    while not state.stop and guess != password:
        guess = ''.join(random.choices(charset, k=len(password)))
        attempts += 1
        yield guess, attempts, round(time.time() - start, 3)
        if guess == password:
            return

def leetspeak_variants(word):
    substitutions = {
        'a': ['a', '@', '4'], 'e': ['e', '3'],
        'i': ['i', '1', '!'], 'o': ['o', '0'],
        's': ['s', '$', '5'], 't': ['t', '7']
    }
    
    variants = set([word])
    
    for i, ch in enumerate(word):
        if ch.lower() in substitutions:
            new_variants = set()
            for variant in variants:
                for sub in substitutions[ch.lower()]:
                    new = variant[:i] + sub + variant[i+1:]
                    new_variants.add(new)
            variants.update(new_variants)
    
    return list(variants)

def dictionary_attack(password, wordlist, state: CrackerState):
    attempts = 0
    start = time.time()

    for word in wordlist:
        if state.stop:
            return
        word = word.strip()
        guesses = [word] + leetspeak_variants(word)
        for guess in guesses:
            if state.stop:
                return
            attempts += 1
            yield guess, attempts, round(time.time() - start, 3)
            if guess == password:
                return
