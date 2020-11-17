public Cell[][] grid;
public int w, h;
public int ts = 20;
ArrayList<Cell> openSet, closedSet, path;
boolean started, initialize = false;

Cell start, end, current;

void setup(){
  size(800, 800);
  w = width/ts;
  h = height/ts;
  openSet = new ArrayList<Cell>();
  closedSet = new ArrayList<Cell>();
  grid = new Cell[w][h];
  for(int i = 0; i < w; i++){
    for(int j = 0; j < h; j++){
      grid[i][j] = new Cell(i, j);
    }
  }
  start = grid[0][0];
  end = grid[w-1][h-1];
  openSet.add(start);
}



void draw(){
  if(started && initialize){init();initialize = false;}
  if(started){
    solve();
  }else{
    display_tiles();
  }
}

void mousePressed(){
  int mx = floor(map(mouseX, 0, width, 0, w));
  int my = floor(map(mouseY, 0, height, 0, h));
  for(int i = 0; i < w; i++){
    for(int j = 0; j < h; j++){
      Cell c = grid[i][j];
      if(mx == c.x && my == c.y){
        c.wall = true;
      }
    }
  }
}

void mouseDragged(){
  int mx = floor(map(mouseX, 0, width, 0, w));
  int my = floor(map(mouseY, 0, height, 0, h));
  for(int i = 0; i < w; i++){
    for(int j = 0; j < h; j++){
      Cell c = grid[i][j];
      if(mx == c.x && my == c.y){
        c.wall = true;
      }
    }
  }
}

void keyPressed() {
  if (key == ENTER && !started) {
    started = true;
    initialize = true;
  }
}

void init(){
  for(int i = 0; i < w; i++){
    for(int j = 0; j < h; j++){
      grid[i][j].find_neighbours();
    }
  }
  
}

void solve(){
    if(openSet.size() > 0){
    current = openSet.get(best_openSet());
    if(current.x == end.x && current.y == end.y){
      //draw best path
      reconstruct_path();
    } else{
    
      openSet.remove(current);
      closedSet.add(current);
    
      for(Cell n: current.neighbours){
        if(!neighbour_in_closedSet(n)){
          float g_temp = current.g + calc_h(current, n);
        
          if(neighbour_in_openSet(n)){
            n.g = g_temp;
            n.h = calc_h(n, end);
            n.f = n.g + n.h;
            n.came_from = current;
          }
        
          if(!neighbour_in_openSet(n)){
            n.g = g_temp;
            n.h = calc_h(n, end);
            n.f = n.g + n.h;
            n.came_from = current;
            openSet.add(n);
          }
        }
        display_tiles();
      }
    }
  }
  
}

void display_tiles(){
  for(int i = 0; i < w; i++){
    for(int j = 0; j < h; j++){
      grid[i][j].display(color(255));
      if(grid[i][j].wall){
        grid[i][j].display(color(0));
      }
    }
  }
  
  
  
  for(Cell c: openSet){
    c.display(color(0, 255, 0));
  }
  
  for(Cell c: closedSet){
    c.display(color(255, 0, 0));
  }
  
  end.display(color(255, 255, 0));
  
}

int best_openSet(){
  int index = 0;
  for(int i = 0; i< openSet.size();i++){
    if(openSet.get(index).f > openSet.get(i).f) index = i;
  }
  return index;
}

boolean neighbour_in_openSet(Cell neighbour){
  for(Cell n: openSet){
    if(n.x == neighbour.x && n.y == neighbour.y) return true;
  }
  return false;
}

boolean neighbour_in_closedSet(Cell neighbour){
  for(Cell c: closedSet){
    if(c.x == neighbour.x && c.y == neighbour.y) return true;
  }
  return false;
}

void reconstruct_path(){
  path = new ArrayList<Cell>();
  while(current.came_from!=null){
    path.add(current);
    current = current.came_from;
  }
  
  for(Cell c: path){
    c.display(color(0, 0, 255));
  }
  start.display(color(0, 0, 255));
  
}

float calc_h(Cell a, Cell b){
    return dist(a.x, a.y, b.x, b.y);
    //return abs( a.x - b.x) + abs(a.y - b.y);
  }
