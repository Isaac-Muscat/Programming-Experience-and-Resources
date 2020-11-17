class Drop {
  float x = random(0, width);
  float y = random(-500, -50);
  float z = random(0, 20);
  float ySpeed = map(z, 0, 20, 4, 10);
  float len = map(z, 0, 20, 10, 20);
  
  void update() {
    y += ySpeed;
    float gravity = map(z, 0, 20, 0, 0.2);
    ySpeed += gravity;
    if (y > height) {
      y = random(-200, -100);
      ySpeed = map(z, 0, 20, 4, 10);
    }
  }
  
  void show() {
    float thickness = map(z, 0, 20, 1, 3);
    strokeWeight(thickness);
    stroke(138, 43, 226);
    line(x, y, x, y+len);
  }
  
}
