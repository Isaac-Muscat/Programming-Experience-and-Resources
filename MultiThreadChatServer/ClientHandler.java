import java.io.*;
import java.net.*;
import java.util.*;

public class ClientHandler extends Thread{
	private Socket client;
	private ObjectInputStream input;
	private ObjectOutputStream output;
	private ArrayList<ClientHandler> clients;

	public ClientHandler (Socket socket, ArrayList<ClientHandler> clients) throws IOException{
		this.client = socket;
		this.clients = clients;
	}

	@Override
	public void run(){
		try {
			setupStreams();
            while(true){
            	String message = (String) input.readObject();
            	outToAll(message);
            }

        } catch (IOException ex) {
            System.out.println("Server exception: " + ex.getMessage());
            ex.printStackTrace();
        }catch (ClassNotFoundException ex){
        	ex.printStackTrace();
        }
	}

	private void setupStreams () throws IOException{
		output = new ObjectOutputStream(client.getOutputStream());
		output.flush();
		input = new ObjectInputStream(client.getInputStream());
	}

	private void outToAll(String text){
		for (ClientHandler aClient : clients){
			try{
				aClient.output.writeObject(text);
			}catch(IOException ex){
				ex.printStackTrace();
			}
		}
	}
}