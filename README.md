# eml-linkunprotect


I was having difficulty analyzing phishing emails because Barracuda email filter was re-writing all the URLs using a link protect feature. While this is a great feature in general, it makes it difficult to do analysis on the phishing emails because none of the popular tools can parse through the protected URLs. 

This is a Python script that accepts an '.eml' file as input, and will output another '.eml' file (in the same directory, it will add "decoded_" to the beginning of the file name) with all of the rewritten URLs back to their original form and ready to be analyzed further.


While this was written specifically for Barracuda, it could be pretty easily modified to any other link protection service. Also, while this was written specifically for '.eml' files, it may work just fine on other text email formats; I just haven't tested it on anything else.

\- H Nielsen 