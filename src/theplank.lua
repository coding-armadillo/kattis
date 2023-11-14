function f(n)
  if n == 0 then
    return 1
  elseif n == 1 then
    return 1
  elseif n == 2 then
    return 2
  else
    return f(n - 1) + f(n - 2) + f(n - 3)
  end
end

n = io.read("*n")
print(f(n))
