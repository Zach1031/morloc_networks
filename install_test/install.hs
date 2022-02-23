import System.Environment
import System.Process
import Data.List
import Control.Concurrent

formatName :: String -> String
formatName string = (init (init (init (init string))))

moveFile :: String -> IO ProcessHandle
moveFile x = runCommand ("morloc make -o " ++ (formatName x) ++ " " ++ x)

startMove :: String -> IO ProcessHandle
startMove args = moveFile args

makeComm :: String -> String
makeComm file = "morloc make -o " ++ (formatName file) ++ " " ++ file

moveComm :: String -> String
moveComm file = "cp " ++ (formatName file) ++ " ~/.local/bin/test"

deleteComm :: String -> String
deleteComm file = "rm " ++ (formatName file)

main = do
    args <- getArgs
    runCommand (makeComm (head args))
    runCommand ("clear")
    print "Created executable"
    threadDelay 1000000

    runCommand (moveComm (head args))
    runCommand ("clear")
    print "Moved to bin"
    threadDelay 10000

    runCommand (deleteComm (head args))
    runCommand ("clear")
    print "Installation Complete"
