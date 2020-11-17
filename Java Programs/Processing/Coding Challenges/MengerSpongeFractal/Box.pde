class Box {
  PVector pos;
  float r;
  
  Box(float x, float y, float z, float r) {
    pos = new PVector(x, y, z);
    this.r = r;
  }
  
  ArrayList<Box> generate() {
    ArrayList<Box> boxes = new ArrayList<Box>();
    for (int x = -1; x < 2; x++) {
      for (int y = -1; y < 2; y++) {
        for (int z = -1; z < 2; z++) {
          
          if(abs(x) + abs(y) + abs(z) >1 ){
            float newR = r/3;
            Box b = new Box(pos.x+x*newR, pos.y+y*newR, pos.z+z*newR, newR);
            boxes.add(b);
          }
        }
      }
    }
    return boxes;
  }
  
  void show() {
    pushMatrix();
    translate(pos.x, pos.y, pos.z);
    fill(255);
    box(r);
    popMatrix();
  }
  
}
