import java.io.*;
import java.net.*;

public class Clienthttp {
    public static void main(String[] args) {
        try {
            if (args.length < 1) {
                System.out.println("Usage: java Clienthttp <hostname>");
                return;
            }

            String host = args[0];
            Socket socket = new Socket(host, 80);
            OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
            InputStreamReader isr = new InputStreamReader(socket.getInputStream());

            BufferedWriter bufOut = new BufferedWriter(osw);
            BufferedReader bufIn = new BufferedReader(isr);

            String request = "GET / HTTP/1.0\r\nHost: " + host + "\r\n\r\n";
            bufOut.write(request);
            bufOut.flush();

            String line;
            while ((line = bufIn.readLine()) != null) {
                System.out.println(line);
            }

            bufIn.close();
            bufOut.close();
            socket.close();
        } catch (IOException e) {
            System.out.println("Erreur: " + e.getMessage());
        }
    }
}

