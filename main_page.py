def main_page(url):

  # Our 'root' directory is pages/.
  # This is where we keep all our web files
  path = 'pages/' + url

  # If the path ends in / then no file name was given
  # Use index.html as the default file name if non given
  if path[-1:] == '/':
    file_name = path + 'index.html'
  else:
    file_name = path

  # Try to open the file and return contents
  # If anything goes wrong return an error message instead  
  try:
    f = open(file_name, 'r')
    output = f.read()
    f.close()
  except:
    output = '<html><body>No file associated with URL %s</body></html>' % file_name
  return(output)