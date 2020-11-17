class Board{
  ArrayList<Piece> pieces;
  boolean white_turn = true;
  boolean black_in_check = false;
  boolean white_in_check = false;
  Board(){
    pieces = new ArrayList<Piece>();
    init_pieces();
  }
  
  void display(){
    display_grid();
    display_pieces();
  }
  
  void init_pieces(){
    for(int i = 0; i<8;i++)pieces.add(new Pawn(i, 6, true));
    pieces.add(new King(4, 7, true));
    pieces.add(new Queen(3, 7, true));
    pieces.add(new Rook(0, 7, true));
    pieces.add(new Rook(7, 7, true));
    pieces.add(new Knight(1, 7, true));
    pieces.add(new Knight(6, 7, true));
    pieces.add(new Bishop(2, 7, true));
    pieces.add(new Bishop(5, 7, true));
    
    for(int i = 0; i<8;i++)pieces.add(new Pawn(i, 1, false));
    pieces.add(new King(4, 0, false));
    pieces.add(new Queen(3, 0, false));
    pieces.add(new Rook(0, 0, false));
    pieces.add(new Rook(7, 0, false));
    pieces.add(new Knight(1, 0, false));
    pieces.add(new Knight(6, 0, false));
    pieces.add(new Bishop(2, 0, false));
    pieces.add(new Bishop(5, 0, false));
  }
  
  void display_grid(){
    int checker;
    for(int y=0;y<8;y++){
      for(int x=0;x<8;x++){
        checker = (x+y)%2;
        fill(138*checker + (1-checker)*250, 71*checker+ (1-checker)*238, 34*checker+ (1-checker)*205);
        rect(x*ts, y*ts, ts, ts);
      }
    }
  }
  
  void display_pieces(){
    Piece selected_piece = null;
    for(Piece p: pieces) {
      if(p.selected)selected_piece = p;
    }
    for(Piece p: pieces) {
      if(pieces.indexOf(p) != pieces.indexOf(selected_piece)){
        pushMatrix();
        imageMode(CENTER);
        translate(p.ax, p.ay);
        image(p.img, 0, 0);
        popMatrix();
      }
    }
    if(selected_piece!=null){
      pushMatrix();
      imageMode(CENTER);
      translate(selected_piece.ax, selected_piece.ay);
      image(selected_piece.img, 0, 0);
      popMatrix();
    }
  }
  
}
