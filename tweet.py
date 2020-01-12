from twython import Twython
import sys

C_key="99qBjjNWFsn86SX2Wyag7EQUn"
C_secret="Wd6mkaFWFu6TZmhWL7dSzUtZ3ZlusElnvXQXkK4tFDjpUS0Wru"
A_token="1215563528968507393-2wqTWZNn4xEHHiNc311xfcAbd5sljP"
A_secret="wpSKF2LCdS225nHgjwPkfJAtwvDRrwPQOryNc2WhpH2Cu"

tweet = Twython(C_key, C_secret, A_token, A_secret)
tweet.update_status(status=sys.argv[1])
