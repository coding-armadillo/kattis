main = do
    input <- getLine
    let n = (read input :: Int)
    if  n `mod` 2  ==  0
    then do putStrLn "Alice"
            putStrLn "1"
        else putStrLn "Bob"
