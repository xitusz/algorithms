def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    for _ in range(low_index, high_index):
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
            is_palindrome_recursive(word, low_index, high_index)
        else:
            return False

    return True


print(is_palindrome_recursive('arara', 0, 4))
print(is_palindrome_recursive('araras', 0, 5))