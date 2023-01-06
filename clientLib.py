# example usage and client library for the endpoint graphql

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


class Atm(object):
    def __init__(self, Endpoint):
        self.transport = AIOHTTPTransport(url=Endpoint)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def auth(self, username, pin):
        query = gql('''
            query auth($pin: String!, $username: String!) {
                token(pin: $pin, username: $username)
            }
        ''')
        params = {"pin": pin, "username": username}
        message = self.client.execute(query, variable_values=params)
        if 'token' in message:
            return message['token']
        else:
            return ''

    def balance(self, auth):
        query = gql('''
            query MyQuery($token: String!) {
                account(token: $token) {
                    balance
                }
            }
        ''')
        params = {"token": auth}
        message = self.client.execute(query, variable_values=params)
        if 'account' in message:
            if 'balance' in message['account']:
                return message['account']['balance']
            else:
                return '0'
        else:
            return '0'

    def withdraw(self, auth, amount):
        query = gql('''
            mutation withdraw($amount: Decimal!, $token: String!) {
                withdraw(token: $token, amount: $amount) {
                    amountChanged
                }
            }
        ''')
        params = {"token": auth, "amount": amount}
        message = self.client.execute(query, variable_values=params)
        if 'withdraw' in message:
            if 'amountChanged' in message['withdraw']:
                return message['withdraw']['amountChanged']
            else:
                return '0'
        else:
            return '0'



    def deposit(self, auth, amount):
        query = gql('''
            mutation deposit($amount: Decimal!, $token: String!) {
                deposit(token: $token, amount: $amount) {
                    amountChanged
                }
            }
        ''')
        params = {"token": auth, "amount": amount}
        message = self.client.execute(query, variable_values=params)
        if 'deposit' in message:
            if 'amountChanged' in message['deposit']:
                return message['deposit']['amountChanged']
            else:
                return '0'
        else:
            return '0'

