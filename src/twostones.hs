main = do
    input <- getLine
    let n = (read input :: Int)
    if  n `mod` 2  ==  1
    then putStrLn "Alice"
        else putStrLn "Bob"
