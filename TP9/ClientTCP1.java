import java.io.*;
import java.net.*;

public class ClientTCP1
{
    public static void main(String[] args) throws IOException 
    {
        Socket socket = new Socket("localhost", 2016 );
        System.out.println("Connection d'un client");
        DataOutputStream dOut = new DataOutputStream (socket.getOutputStream());
        dOut.writeUTF("message test");
        socket.close();
    }
}

