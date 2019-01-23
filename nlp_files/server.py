from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from halogen import login, singup
from main_function import get_answer

class ChatServer(WebSocket):
        
    def handleMessage(self):
        # echo message back to client
        message = self.data
        message_array = message.split(',')
        message_sender = message_array.pop()
        response = 'error'
        if message_sender == 'login':
            response = login(message_array)

        if message_sender == 'singup':
            response = singup(message_array)

        if message_sender == 'proceed':
            response = 'proceed'

        if message_sender == 'yes':
            response = get_answer('yes,'.join(message_array))
            print('Question Responsed.')

        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


server = SimpleWebSocketServer('', 8008, ChatServer)
server.serveforever()
