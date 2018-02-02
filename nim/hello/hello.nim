proc hello(): string =
  echo "What's your name? "
  var name: string = readLine(stdin)
  return "Hi, " & name & "!"

echo hello()
