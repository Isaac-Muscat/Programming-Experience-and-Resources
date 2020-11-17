import java.awt.event.*;
import javax.swing.JPanel;
import java.awt.*;
import java.awt.image.BufferedImage;

public class SnakeGame extends JPanel implements KeyListener, Runnable {

 private int width = 600;
 private int height = 600;
 Graphics bbg;
 BufferedImage img;
 Snake snake;
 Token token;
 Thread t;
 Dimension gBounds;
 boolean gameStarted;
 boolean gameOver;
 
 public SnakeGame() {
  setPreferredSize(new Dimension(width, height));
  gBounds = new Dimension(width, height);
  gameStarted = false;
  gameOver = false;
  img = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
  bbg = img.createGraphics();
  snake = new Snake(20, width/2, height/2, Snake.EAST, new Dimension(width, height));
  token = new Token(snake, new Dimension(width, height));
  addKeyListener(this);
  setFocusable(true);
  start();
 }
 
 public void start() {
   
  t = new Thread(this);
  t.start();
 }
 
 public void stop() {
 }
 
 public void resized(int w, int h) {
   width = w;
   height = h;
   img = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
   bbg = img.createGraphics();
   snake.setBounds(new Dimension(width, height));
   token.setBounds(new Dimension(width, height));
 }
 
 
 public void paint(Graphics g) {
  super.paintComponent(g);
  if (gameOver == false) {
   bbg.setColor(Color.BLACK);
   bbg.fillRect(0, 0, width, height);
   snake.paint(bbg);
   token.paint(bbg);
   g.drawImage(img, 0, 0, null);
  } else {
   g.setColor(Color.BLACK);
   g.fillRect(0, 0, width, height);
   g.setColor(Color.WHITE);
   g.drawString("Game Over", width/2-40, height/4);
  }
 }
 

 @Override
 public void run() {
  while (gameOver == false) {
   if (snake.checkCollision() == false) {
    if (gameStarted) {
     snake.move();
    }
   } else{
    gameOver = true;
    try {
     t.sleep(500);
    } catch (Exception e) {}
    repaint();
    stop();
   }
   repaint();
   try {
    t.sleep(30);
   } catch(Exception e) {}
  }
 }


 
 @Override
 public void keyPressed(KeyEvent e) {
   if (gameStarted == false)
     gameStarted  = true;
   
   if (e.getKeyCode() == KeyEvent.VK_UP)
     snake.setDirection(Snake.NORTH);
   else if (e.getKeyCode() == KeyEvent.VK_DOWN)
     snake.setDirection(Snake.SOUTH);
   else if (e.getKeyCode() == KeyEvent.VK_RIGHT)
     snake.setDirection(Snake.EAST);
   else if (e.getKeyCode() == KeyEvent.VK_LEFT)
     snake.setDirection(Snake.WEST);
   
   try {
     Thread.sleep(10);
   } catch (Exception e1) {}
   
 }

 @Override
 public void keyReleased(KeyEvent arg0) {}

 @Override
 public void keyTyped(KeyEvent arg0) {}

}