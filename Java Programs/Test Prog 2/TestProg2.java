
import java.util.*;

public class TestProg2 {
  
  public static int x = 1;
  public static int y = 1;
  public static ArrayList<Block> body;
  public static int length = 10;
  public static void main(String[] args){
    
    body = new ArrayList();
    
    for (int i = 1; i <= length;i++){
    body.add(new Block(x, y));
    x+=1;
    y+=2;
    }
    
    for (int i = 0; i < body.size(); i++){
    System.out.println(body.get(i).getX());
    System.out.println(body.get(i).getY());
    }
    
    
  }
}