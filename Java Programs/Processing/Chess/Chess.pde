Board board;
public int ts;
public PImage chess_pieces;
int mx, my;
Piece removed;

void setup(){
  size(800, 800);
  background(255);
  chess_pieces = loadImage("Chess_Pieces.png");
  ts = width/8;
  board = new Board();
  removed = null;
}


void draw(){
  board.display();
}

void map_mouse(){
  mx = floor(map(mouseX, 0, width, 0, 8));
  my = floor(map(mouseY, 0, height, 0, 8));
}

void mousePressed(){
  map_mouse();
  for(Piece p: board.pieces){
    if(mx == p.x && my == p.y && board.white_turn == p.white) p.selected = true;
  }
}

void mouseDragged() {
  for(Piece p: board.pieces){
    if(p.selected == true){
      p.ax = mouseX;
      p.ay = mouseY;
    }
  }
}

void mouseReleased(){
  for(Piece p: board.pieces){
    if(p.selected == true){
      int x2 = floor(map(p.ax, 0, width, 0, 8));
      int y2 = floor(map(p.ay, 0, width, 0, 8));
      if(p.can_move(x2, y2, board, board.pieces.indexOf(p))){
        p.x = x2;
        p.y = y2;
        removed = p.check_taken(x2, y2, board, board.pieces.indexOf(p));
        board.white_turn = !board.white_turn;
      }
        p.snap_piece();
        p.selected = false;
      
    }
  }
  if(removed != null)board.pieces.remove(removed);
}
