import System.Process


formatName :: String -> String
formatName string = (init (init (init (init string))))
