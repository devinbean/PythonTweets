import twitter

api = twitter.Api(consumer_key='W16x5AHsPd3OMn3vzC04fg', consumer_secret='6z0nUQ7kH66f8IlVaqPqsy4JUyq9EhQIK2zSd7Ahfs', access_token_key='288951576-eGThyIKfPut2jmv5kF5QrphshIk4AMIUgXakqAEx', access_token_secret='5m76lTboTVpQY1R5naOiRLclSPvDP7dtWYuvF7VoyW0') 

cred = api.VerifyCredentials()

print cred

