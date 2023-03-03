function fibonacci(n)
  if n < 2 then 
    return n
  else 
    return fibonacci(n-1) + fibonacci(n-2)
  end 
end

--print the first 10 Fibonacci Numbers
for i = 0,9
  print(fibonacci(i)
end
