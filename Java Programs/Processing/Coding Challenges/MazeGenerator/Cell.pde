

class Cell{
  int x, y;
  boolean[] walls = {true, true, true, true};
  int scale = MazeGenerator.scale;
  boolean visited = false;
  
  public Cell(int x, int y){
    this.x = x;
    this.y = y;
  }
  
  public void show(){
    int x = this.x*scale;
    int y = this.y*scale;
    if (visited){
      noStroke();
      fill(200);
      rect(x,y,scale,scale);
    }
    stroke(0);
    
    if(walls[0]){
      line(x, y, x + scale, y);
    }
    if(walls[1]){
      line(x+scale, y, x + scale, y+scale);
    }
    if(walls[2]){
      line(x, y+scale, x + scale, y+scale);
    }
    if(walls[3]){
      line(x, y, x, y+scale);
    }
    
  }
  
  public void highlight(){
    int x = this.x*scale;
    int y = this.y*scale;
    noStroke();
    fill(255,0,0);
    rect(x+scale/4,y+scale/4,scale/2,scale/2);
  }
  
  
}
