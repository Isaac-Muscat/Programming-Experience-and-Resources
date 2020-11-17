class Star {
  float x;
  float y;
  float z;
  float pz;
  float c = random(0, 255);
  
  Star() {
    x = random(-width/2, width/2);
    y = random(-height/2, height/2);
    z = random(width);
    pz = z;
  }
  
  void update() { 
    z -= speed;
    if (z < 1) {
      z = width;
      x = random(-width/2, width/2);
      y = random(-height/2, height/2);
      pz = z;
    }
  }
  
  void show() {
    
    float sx = map(x/z, 0, 1, 0, width);
    float sy = map(y/z, 0, 1, 0, height);
    float r = map(z, 0, width, 1, 0)*(maxSpeed-speed);
    
    
    float px = map(x/pz, 0, 1, 0, width);
    float py = map(y/pz, 0, 1, 0, width);
    
    pz = z;
    
    stroke(c, c/2, 0);
    line(sx, sy, px, py);
    
    fill(c, c/2, 0);
    noStroke();
    ellipse(sx, sy ,r ,r);
  }
  
}
