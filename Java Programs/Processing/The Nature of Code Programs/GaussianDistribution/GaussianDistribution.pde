import java.util.Random;

Random generator;
void setup(){
  size(400,300);
  generator=new Random();
}

void draw(){
  background(255);
  
  float h = (float)generator.nextGaussian();
  
  fill(0);
  ellipse(width/2,height/2,h,h);
}
