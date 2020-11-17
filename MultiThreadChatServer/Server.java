import java.net.*;
import java.io.*;
import java.util.*;

public class Server {
	
	public final int PORT = 6789;
	private static ArrayList<ClientHandler> clients;

	private ObjectOutputStream output;
	private ObjectInputStream input;
	private ServerSocket server;
	private Socket client;

	public Server(){
		clients = new ArrayList<ClientHandler>();
	}

	private void startRunning(){
		try{
			server = new ServerSocket(PORT);
            System.out.println("Server is listening on port " + PORT);

            while (true) {
                client = server.accept();
                System.out.println("New client connected");
                ClientHandler newClient = new ClientHandler(client, clients);
                clients.add(newClient);
                newClient.start();
            }
 
        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }
	}

	public static void main(String[] args){
		Server server = new Server();
		server.startRunning();
	}
}