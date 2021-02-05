def username_generator(first_name, last_name):
  #now i have a length
  fnLength = len(first_name)
  lnLength = len(last_name)

  if fnLength > 3:
    firstSlice = first_name[:3]
  else:
    firstSlice = first_name

  if lnLength > 4:
    lastSlice = last_name[:4]
  else:
    lastSlice - last_name
  username = firstSlice+lastSlice
  return username

def password_generator(username):
    password = ""
    for letters in range(0, len(username)):
        password += username[letters-1]
    return password
pw = password_generator("RyaRome")
print(pw)
