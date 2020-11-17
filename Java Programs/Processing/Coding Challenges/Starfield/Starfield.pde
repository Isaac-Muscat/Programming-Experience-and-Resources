float topSpeed, speed;
float deltaSpeed = 0.5;
float maxSpeed = 50;
//Star[] stars = new Star[int(20000/maxSpeed)];
Star[] stars = new Star[2000];
void setup() {
  size(800, 800);
  translate(width/2, height/2);
  for (int i = 0; i < stars.length; i++) {
    stars[i] = new Star();
  }
}

void draw() {
  background(0);
  float distance = dist(mouseX, mouseY, width/2, height/2);
  if (distance >= width/2) distance = width/2-1;
  topSpeed = map(distance, 0, width/2, maxSpeed, 0);
  if (topSpeed > speed) {
    speed += deltaSpeed;
  } else if (topSpeed < speed) {
    speed -= deltaSpeed;
  } else {
    speed = topSpeed;
  }
  
  translate(width/2, height/2);
  for (int i = 0; i < stars.length; i++) {
    stars[i].update();
    stars[i].show();
  }
  displayShip();
  
}

void displayShip() {
  fill(50);
  noStroke();
  ellipse(0, 0-speed/20, speed/3, speed/10);
  ellipse(0, 0, speed, speed/10);
  fill(255, 80, 10); 
  ellipse(0 - speed/10, 0+speed/20, speed/10, (speed/10));
  ellipse(0 + speed/10, 0+speed/20, speed/10, (speed/10));
}
