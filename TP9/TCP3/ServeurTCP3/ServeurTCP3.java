import java.io.*;
import java.net.*;

public class ServeurTCP3 
{
    public static void main(String[] args) throws IOException 
  {
        ServerSocket socketserver = new ServerSocket(2016);
        System.out.println("Serveur en attente");

        while (true) 
      {
            try 
            {
                Socket socket = socketserver.accept();
                System.out.println("Connexion d'un client");

                DataInputStream dIn = new DataInputStream(socket.getInputStream());
                DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());

                String message = dIn.readUTF();
                System.out.println("Message reçu: " + message);

                String rev = new StringBuilder(message).reverse().toString();
                dOut.writeUTF(rev);
                dOut.flush();

                socket.close();
            } catch (SocketException e) 
            {
                System.out.println("SocketException: " + e.getMessage());
            }
        }
    }
}

