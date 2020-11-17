import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Client extends JFrame{

	public String name = "";
	private JTextField userText;
	private JTextArea chatWindow;
	private ObjectOutputStream output;
	private ObjectInputStream input;
	private String message = "";
	private String serverIP;
	private Socket socket;

	public Client(String host, String n){
		super(n + " - Instant Messanger");
		this.name = n;
		serverIP = host;
		setupGUI();
	}

	public void startRunning(){
		try{
			connectToServer();
			setupStreams();
			whileChatting();
		}catch(EOFException ex){
			showMessage("\n Client Terminated connection!");
		}catch(IOException ex){
			ex.printStackTrace();
		}finally{
			closeCrap();
		}
	}

	private void connectToServer() throws IOException{
		showMessage("Attempting connection... \n");
		socket = new Socket(InetAddress.getByName(serverIP), 6789);
		showMessage("Connected to:" + socket.getInetAddress().getHostName());
	}

	private void setupStreams() throws IOException{
		output = new ObjectOutputStream(socket.getOutputStream());
		output.flush();
		input = new ObjectInputStream(socket.getInputStream());
		showMessage("\n Streams are good!");
	}

	private void whileChatting() throws IOException{
		ableToType(true);
		while(true){
			try{
				message = (String) input.readObject();
				showMessage("\n"+message);
			}catch(ClassNotFoundException ex){
				showMessage("\n I don't know that type!");
			}
		}
	}

	private void closeCrap(){
		showMessage("\n closing crap down...");
		ableToType(false);
		try{
			output.close();
			input.close();
			socket.close();
		}catch(IOException ex){
			ex.printStackTrace();
		}
	}

	private void sendMessage(String m){
		try{
			output.writeObject(name + " - " + m);
			output.flush();
			//showMessage("\nClient - " + m);
		}catch(IOException ex){
			chatWindow.append("\n Something went wrong!");
		}
	}

	private void showMessage(final String m){
		SwingUtilities.invokeLater(
			new Runnable(){
				public void run(){
					chatWindow.append(m);
				}
			}
		);
	}

	private void ableToType(final boolean tof){
		SwingUtilities.invokeLater(
			new Runnable(){
				public void run(){
					userText.setEditable(tof);
				}
			}
		);
	}

	public static void main(String[] args){
		if (args.length < 1) return;
		Client client = new Client("127.0.0.1", args[0]);
		client.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		client.startRunning();
	}

	private void setupGUI(){
		userText = new JTextField();
		userText.setEditable(false);
		userText.addActionListener(
			new ActionListener(){
				public void actionPerformed(ActionEvent event){
					sendMessage(event.getActionCommand());
					userText.setText("");
				}
			}
		);
		add(userText, BorderLayout.NORTH);
		chatWindow = new JTextArea();
		add(new JScrollPane(chatWindow), BorderLayout.CENTER);
		setSize(300, 150);
		setVisible(true);
	}
}