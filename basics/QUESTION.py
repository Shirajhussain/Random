#
# s = input('Enter some string to Reverse')
# output = s[::-1]
# print(output)
#
#
# s= input('Enter some string to Reverse')
# r=reversed(s)
# output=''.join(r)
# print(output)


# s=input('Enter some string to reverse:')
# output=''
# i=len(s)-1
# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)

# s = input('Enter Some String:')
# words = s.split()
# w = words[::-1]
# output = ''.join(w)
# print(output)

# s = input('Enter Any String:')
# words = s.split()
# output = []
# for word in words:
#     output.append(word[::-1])
# output = ' '.join(output)
# print(output)

# s='one two three four five six' # Input string
# l=s.split()  # Split the string into a list of words
# l1=[]        # Initialize an empty list to store processed words
# i=0          # Initialize index variable
#
# print(len(l)):
# # Process each word
# while i<len(l):
#     if i%2 == 0:   # If the index is even
#         l1.append(l[i])    # Append the word as it is
#     else:          # If the index is odd
#         l1.append(l[i][::-1])    # Reverse the word and append it
#     i=i+1   # Increment the index
#
# # Join the processed words into a single string
# output=''.join(l1)
# print(output)

# s=input('enter input string:')
# print('Characters presnt at even Index:')
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1

#
# s1='RAVI'
# s2='TEJA'
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     output=output+s1[i]+s2[j]
#     i=i+1
#     j=j+1
# print(output)


s1 = 'RAVI'
s2 = 'TEJAjhjh'
output = ''
i, j = 0, 0

while i < len(s1) or j < len(s2):
    if i < len(s1):  # Ensure `i` is within bounds of `s1`
        output += s1[i]
        i += 1
    if j < len(s2):  # Ensure `j` is within bounds of `s2`
        output += s2[j]
        j += 1

print(output)



