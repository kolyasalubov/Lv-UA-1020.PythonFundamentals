#task 1
philosophy_string = 'Beautiful is better than ugly.'

better_count = philosophy_string.count('better')
never_count = philosophy_string.count('never')
is_count = philosophy_string.count('is')

print(f'String contain better {better_count} times\n'
      f'String contain better {never_count} times\n'
      f'String contain better {is_count} times')

#task 2
print(philosophy_string.upper())

#task 3
print(philosophy_string.replace('is', '&'))